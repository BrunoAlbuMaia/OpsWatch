from Application.program import DependencyContainer



class PluginController:
    injection = DependencyContainer()
 
    def __init__(self) -> None:
        self.plugin_manager_service = self.injection.pluginManager
    async def upload_plugin(self,  hook_file, plugin_file):
        try:
            retorno = await self.plugin_manager_service.upload_plugin( hook_file, plugin_file)
            return retorno
        except Exception as e:
            raise Exception(str(e))
        
    async def atualizar_plugin(self,new_hook_file, new_plugin_file):
        pass