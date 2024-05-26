from Domain.Interface.IPluginManagerService import IPluginManagerService
from Infrastruncture.CrossCutting.plugins.plugin_manager import PluginManager
import os
import shutil
from decouple import config

HOOKS_DIR = config('pasta_hooks')
PLUGINS_DIR = config('pasta_plugins')

class PluginManagerService(IPluginManagerService):
    def __init__(self):
        self.plugin_managers = {}

    async def add_plugin_manager(self,  nome_arquivo_hooks, nome_arquivo_plugin):
        self.plugin_managers[nome_arquivo_plugin] = PluginManager(nome_arquivo_plugin=nome_arquivo_plugin,nome_arquivo_hooks=nome_arquivo_hooks)


    async def upload_plugin(self, hook_file, plugin_file):
        try:
            hook_save_path = os.path.join(HOOKS_DIR, hook_file.filename)
            plugin_save_path = os.path.join(PLUGINS_DIR, plugin_file.filename)

            with open(hook_save_path, "wb") as hook_buffer:
                shutil.copyfileobj(hook_file.file, hook_buffer)

            with open(plugin_save_path, "wb") as plugin_buffer:
                shutil.copyfileobj(plugin_file.file, plugin_buffer)

            return {"message": "Files uploaded feito com sucesso"}
        except Exception as ex:
            raise Exception(str(ex))


    async def execute_plugin_hook(self, name, hook_name, *args, **kwargs):
        if name in self.plugin_managers:
            return await self.plugin_managers[name].execute_hook(hook_name, *args, **kwargs)
        else:
            print(f"Plugin manager '{name}' não encontrado.")
            return []