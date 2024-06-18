from Domain.Interface.IPluginManagerService import IPluginManagerService

from plugins.plugin_manager import PluginManager
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

    async def listar_plugins(self):
        plugins_disponiveis = set()
        for root, dirs, files in os.walk(PLUGINS_DIR):
            for file in files:
                if file.endswith('.py') and file != '__init__.py':
                    plugin_name = file[:-3]  # Remove a extensão .py
                    plugins_disponiveis.add(plugin_name)
        return list(plugins_disponiveis)
    
    async def upload_plugin(self, hook_file, plugin_file):
        try:
            hook_save_path = os.path.join(HOOKS_DIR, hook_file.filename)
            plugin_save_path = os.path.join(PLUGINS_DIR, plugin_file.filename)

            with open(hook_save_path, "wb") as hook_buffer:
                shutil.copyfileobj(hook_file.file, hook_buffer)

            with open(plugin_save_path, "wb") as plugin_buffer:
                shutil.copyfileobj(plugin_file.file, plugin_buffer)

            return {"message": "Arquivo importado com sucesso, seu plugin já está disponível"}
        except Exception as ex:
            raise Exception(str(ex))


    async def execute_plugin_hook(self, name, hook_name, *args, **kwargs):
        if name in self.plugin_managers:
            return await self.plugin_managers[name].execute_hook(hook_name, *args, **kwargs)
        print(f"O Plugin '{name}' não foi encontrado encontrado.")
        return []

    
