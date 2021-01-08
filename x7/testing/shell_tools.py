"""Devtools entry points to be called from Python shell"""


def maketests(module=None, really=False, force=False):
    """Generate/update tests for python module"""
    import sys
    import x7.testing.maketests.maketests as maketests_mod
    if not module:
        print('Help: maketests(module-name, really=False, force=False)')
        print('Example: maketests("x7.sample.needs_test", True)')
    else:
        saved = sys.argv[:]
        try:
            sys.argv = ['--verbose', '--verbose']
            if not really:
                sys.argv.append('--dry-run')
            if force:
                sys.argv.append('--force')
            sys.argv.append(module)
            print('Maketests: argv=', sys.argv)
            maketests_mod.main()
        finally:
            sys.argv = saved


def tools():
    """Help for tools"""
    print('Help for tools')
    for n in _all_tools():
        f = globals()[n]
        if callable(f):
            print('  %s - %s' % (n, f.__doc__))


def _all_tools():
    return [k for k in sorted(globals().keys()) if not k.startswith(('_', 'do_import'))]


def do_import(other_globals: dict):
    """Import appropriate symbols into <other_globals>"""

    for n in _all_tools():
        other_globals[n] = globals()[n]
    other_globals['__all__'] = _all_tools()
    print("Tools imported.  Commands: %s" % ', '.join(t + '()' for t in _all_tools()))
