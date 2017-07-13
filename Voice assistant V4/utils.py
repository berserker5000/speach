import os


def plugins_list(plugins_dirs):
    """ List all python modules in specified plugins folders """
    for path in plugins_dirs.split(os.pathsep):
        for filename in os.listdir(path):
            name, ext = os.path.splitext(filename)
            if ext.endswith(".py"):
                yield name


def import_plugins(plugins_dirs, env):
    """ Import modules into specified environment (symbol table) """
    for p in plugins_list(plugins_dirs):
        m = __import__(p, env)
        env[p] = m