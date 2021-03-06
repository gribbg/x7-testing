import importlib
import inspect
import ast
from typing import Dict, List, Tuple, Union

from x7.lib import annotations
from x7.lib import inspect_more
from x7.testing.maketests import mod_support
from x7.testing.maketests.mod_support import mod_split
from x7.testing.maketests.parse import parse_module
from x7.testing.maketests.types import OptStr, DictTested, DictAdded, ClassSrcInfo, Module


class OutputMapElem(object):
    """Data for a single line of OutputMap"""
    def __init__(self, tag: OptStr, method: OptStr, line: str):
        self.tag = tag
        self.method = method
        self.lines = [line]

    def text(self):
        return ''.join(self.lines)

    def __str__(self):
        return '%-29s %-15s %s' % (
            self.tag or '             -',
            self.method or '       -',
            self.text().rstrip()
        )

    def extend(self, lines: List[str]):
        self.lines.extend(lines)


class OutputMap(object):
    """
        Representation of output file where lines are tagged by which functions/class
        they belong to as well as helpful maps for understanding the file.

        New lines can be appended anywhere by using OutputMap.lines[int].extend(List[str]).
        The insertion point is (usually) OutputMap.classes[str].last
    """
    def __init__(self, verbose: bool, debug=False):
        self.lines: List[OutputMapElem] = []
        self.testmap = {}               # tested_class/module -> testing_class
        self.classes = {}               # classname -> (insert-point, class)
        self.tested: DictTested = {}    # funcname -> implemented_function
        self.added: DictAdded = {}      # classname -> (insert-point, class)
        self.modname = None
        self.module = None
        self.verbose = verbose
        self.debug = debug
        self.imports: Dict[Tuple[str, str], int] = {}   # (mod_head, mod_tail) -> line_number

    def find_class_source(self, cls, lines):
        """Find the first and last+1 lines of cls.  Expand inspect.getsourcelines() result"""
        src_lines, start = inspect.getsourcelines(cls)
        start = start - 1           # Move from 1 based to 0 based counting
        last = start + len(src_lines)
        # Include any non-blank lines, non-indented lines before class definition
        while start-1 > 0 and lines[start-1].rstrip() and not lines[start-1].rstrip().startswith((' ', '\t')):
            start = start-1
        if self.debug:  # pragma: no cover
            for ln in range(start - 5, min(start + 3, len(lines))):
                tag = '*' if ln == start or ln == last else '=' if start < ln < last else ':'
                print('FCS: %4d%s %r' % (ln, tag, lines[ln]))
            print('FCS: %d->%d' % (start, last))
        return start, last

    def build(self, module: Union[str, Module]):
        """Parse <module> and update relevant fields"""

        if isinstance(module, Module):
            self.module = module
            self.modname = module.__name__
        else:
            self.module = None
            self.modname = module
            return

        self.module = importlib.import_module(self.modname)
        dst = parse_module(self.module, self.debug)
        mod_lines, start_line = inspect.getsourcelines(dst.module)
        if self.debug:  # pragma: no cover
            print('%s: %d lines @ %d' % (self.modname, len(mod_lines), start_line))
        self.lines = [OutputMapElem(None, None, l) for l in mod_lines]

        # TODO-do we need this extra blank line?  Seems to just grow the output file
        # if self.lines[-1].lines != ['\n']:
        #     self.lines.append(OutputMapElem(None, None, '\n'))
        for name, cls in dst.classes.items():
            tests = annotations.tested_by(cls)
            if self.verbose:
                tag = '' if mod_support.is_local(cls, self.module) else 'Non-local '

                print('  %sClass: %s -> tests %s' % (tag, cls.__name__, ', '.join(sorted(tests))))
            if mod_support.is_local(cls, self.module):
                cls_start, cls_last = self.find_class_source(cls, mod_lines)
                self.classes[cls.__name__] = ClassSrcInfo(cls, cls_start, cls_last)
                for t in tests:
                    self.testmap[t] = cls.__name__
                    self.tested[t] = inspect_more.item_name(cls)
                if self.debug:  # pragma: no cover
                    print('    %s: %d lines @ %d. Ins @ %d' % (cls.__name__, cls_last - cls_start, cls_start, self.classes[cls.__name__].start))

                for ln in range(cls_start, cls_last):
                    self.lines[ln].tag = cls.__name__
                for member, func in inspect.getmembers(cls, inspect.isfunction):
                    if not member.startswith('test_'):
                        # print('  skipping %s' % m)
                        continue
                    tests = annotations.tested_by(func)
                    if self.debug:  # pragma: no cover
                        print('    func: %s -> tests %s' % (member, ', '.join(sorted(tests))))
                    for t in tests:
                        self.tested[t] = member
                    f_lines, f_start = inspect.getsourcelines(func)
                    if self.debug:  # pragma: no cover
                        print('    %s: %d lines @ %d' % (member, len(f_lines), f_start))
                    for ln, l in enumerate(f_lines, f_start - 1):
                        self.lines[ln].method = member
        for name, info in self.classes.items():
            self.lines[info.start].tag = name + ':ins'

        lines = ''.join(l.text() for l in self.lines)
        if self.debug:                  # pragma: no cover
            print('OutMap: ', self.modname, self.module.__file__)
        parsed = ast.parse(lines)
        self.imports = {}
        for b in parsed.body:
            if isinstance(b, ast.Import):
                for n in b.names:
                    if self.debug:      # pragma: no cover
                        print('   Import: %s%s @ %d' % (n.name, ('as %s' % n.asname) if n.asname else '', b.lineno))
                    if not n.asname:
                        self.imports[mod_split(n.name)] = b.lineno-1
            elif isinstance(b, ast.ImportFrom):
                for n in b.names:
                    if self.debug:      # pragma: no cover
                        print('   ImportFrom: %s -> %s%s%s @ %d' % (
                            b.module, n.name,
                            (' as %s' % n.asname) if n.asname else '',
                            (' level %d' % b.level) if b.level else '',
                            b.lineno)
                        )
                    if not n.asname:
                        self.imports[(b.module, n.name)] = b.lineno-1

        if self.debug:      # pragma: no cover
            import pprint
            pprint.pprint({'     IMPORTS:': self.imports})
