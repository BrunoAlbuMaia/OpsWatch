import pluggy
import importlib.util
import os

# Constante para o diretório padrão de plugins
DEFAULT_PLUGIN_DIRECTORY = 'Infrastruncture/CrossCutting/plugins'

class PluginManager:
    def __init__(self, nome_arquivo_hooks,nome_arquivo_plugin, plugin_directory=DEFAULT_PLUGIN_DIRECTORY):
        self.plugin_directory = plugin_directory
        self.nome_arquivo_plugin = nome_arquivo_plugin
        self.plugin_manager = pluggy.PluginManager(self.nome_arquivo_plugin)
        hooks = self.load_hooks(nome_arquivo_hooks)
        self.plugin_manager.add_hookspecs(hooks)
        self.load_plugins()

    def load_plugins(self):
        for filename in os.listdir(f'{self.plugin_directory}/plugins'):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module_path = os.path.join(f'{self.plugin_directory}/plugins', filename)
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.plugin_manager.register(module)
    def load_hooks(self,nome_arquivo):
        
        file_path = f'{self.plugin_directory}/hooks/{nome_arquivo}.py'
        spec = importlib.util.spec_from_file_location(nome_arquivo, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    async def execute_hook(self, hook_name, *args, **kwargs):
        try:
            hook = getattr(self.plugin_manager.hook, hook_name)
            # Chamar a função de cada implementação de hook
            results = [await impl.function(*args, **kwargs) for impl in hook.get_hookimpls()]
            return results
        except AttributeError:
            print(f"Hook '{hook_name}' não encontrado.")
            return []
        except Exception as e:
            #vai para o arquivo de logue como ERRO
            print(f"Erro ao executar hook '{hook_name}': {e}")
            return []
