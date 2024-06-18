from abc import ABC, abstractmethod

class IPluginManagerService:
    @abstractmethod
    async def add_plugin_manager(self, nome_arquivo_hooks, nome_arquivo_plugin):
        pass
    @abstractmethod
    async def listar_plugins(self):
        pass
    @abstractmethod
    async def upload_plugin(self, hook_file, plugin_file):
        pass
    @abstractmethod
    async def execute_plugin_hook(self, hook_name, *args, **kwargs):
        pass
