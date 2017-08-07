import os
import sys


class SystemInformation(object):
    def getPluginList(self):
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        plugins_directory = cur_dir + "/Plugins"
        sys.path.append(plugins_directory)
        list_of_instances = set()
        for file_name in os.listdir(plugins_directory):
            if file_name == "__init__.py":
                pass
            elif file_name.endswith(".py"):
                list_of_instances.add(file_name.split(".")[0])
            else:
                pass
        return list_of_instances

    def getImportedModules(self):
        return set(sys.modules.keys())

    def getImportedPlugins(self):
        # imported_plugins = list()
        plugins = self.getPluginList()
        modules = self.getImportedModules()
        # for plugin in plugins:
        #     for module in modules:
        #         if plugin == module:
        #             imported_plugins.append(plugin)
        imported_plugins = modules.intersection(plugins)
        return imported_plugins