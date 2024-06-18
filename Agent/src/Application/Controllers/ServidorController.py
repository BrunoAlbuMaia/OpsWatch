from ..program import DependencyContainer


class ServidorController:
    injection = DependencyContainer()
    def __init__(self) -> None:
        self.__configService = self.injection.configService

    async def configurar_servidor_automaticamente(self):
        return await self.__configService.configurar_servidor_automaticamente()
        

