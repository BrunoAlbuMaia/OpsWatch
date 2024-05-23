from Domain.Interface.IPluginManagerService import IPluginManagerService
from Infrastruncture.CrossCutting.plugins.plugin_manager import PluginManager


class PluginManagerService(IPluginManagerService):
    def __init__(self):
        self.plugin_managers = {}

    async def add_plugin_manager(self, name):
        self.plugin_managers[name] = PluginManager(nome_arquivo='hooks',hook_name=name)


    async def upload_plugin(self, name, file):
        if name in self.plugin_managers:
            self.plugin_managers[name].load_plugins()
        else:
            print(f"Plugin manager '{name}' não encontrado.")


    async def execute_plugin_hook(self, name, hook_name, *args, **kwargs):
        if name in self.plugin_managers:
            return await self.plugin_managers[name].execute_hook(hook_name, *args, **kwargs)
        else:
            print(f"Plugin manager '{name}' não encontrado.")
            return []