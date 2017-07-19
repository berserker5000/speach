import os
import sys

path_name = "./Plugins"

import imp


def load_from_file(filepath):
    """Initializing of all classes"""

    class_inst = None
    expected_class = filepath.split("/")[-1].split(".py")[0]

    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

    if file_ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, filepath)

    elif file_ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, filepath)

    if hasattr(py_mod, expected_class):
        class_inst = getattr(py_mod, expected_class)()
    else:
        print expected_class + " not found in " + filepath

    return class_inst


def load_plugins(path):
    """Importing all plugins from Plugins folder.
    Returns list of initialized plugins. Can be provided to Processor"""

    sys.path.append(path)
    list_of_instances = list()
    for file_name in os.listdir(path):
        if file_name == "__init__.py":
            pass
        elif file_name.endswith(".py"):
            print "IMPORTING: " + path + "/" + file_name
            __import__(file_name.split(".py")[0])
            list_of_instances.append(load_from_file(path + "/" + file_name))
        else:
            pass
    return list_of_instances