import imp
import os
import sys

from TextColors import bcolors

cur_dir = os.path.dirname(os.path.abspath(__file__))
plugins_directory = cur_dir + "/Plugins"


def load_module_from_file(filepath):
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
        return bcolors().Red + expected_class + " not found in " + filepath + bcolors().ENDC

    return class_inst


def load_plugins(path=plugins_directory):
    """Importing all plugins from Plugins folder.
    Returns list of initialized plugins. Can be provided to Processor"""

    sys.path.append(path)
    list_of_instances = list()
    for file_name in os.listdir(path):
        if file_name == "__init__.py":
            pass
        elif file_name.endswith(".py"):
            print bcolors().YellowFill + "IMPORTING Plugin: " + bcolors().ENDC + file_name.split(".")[0]
            __import__(file_name.split(".py")[0])
            list_of_instances.append(load_module_from_file(path + "/" + file_name))
        else:
            pass
    return list_of_instances