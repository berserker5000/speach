import imp
import os
import sys

from TextColors import bcolors

cur_dir = os.path.dirname(os.path.abspath(__file__))
outputs_directory = cur_dir + "/Outputs"


class Inputs(object):
    def load_output_from_file(self, filepath):
        input_inst = None
        expected_class = filepath.split("/")[-1].split(".py")[0]

        mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)

        if hasattr(py_mod, expected_class):
            input_inst = getattr(py_mod, expected_class)()
        else:
            return bcolors().FAIL + expected_class + " not found in " + filepath + bcolors().ENDC

        return input_inst

    def getOutputList(self, path=outputs_directory):
        sys.path.append(path)
        inputs_dict = dict()
        for file in os.listdir(path):
            if file == "__init__.py":
                pass
            elif file.endswith(".py"):
                inputs_dict[file.split(".py")[0]] = self.load_output_from_file(path + "/" + file)
            else:
                pass
        return inputs_dict