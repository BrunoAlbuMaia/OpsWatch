import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))

from Application.Controllers.ConfigurarServidorController import ConfigurarServidorController
from Domain.Entites.ConfigServidorEntity import ConfigServidorEntity
from Infrastruncture.CrossCutting.plugins.plugin_manager import PluginManager


from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

router  = APIRouter(tags=['ConfigurarServidor'])
__controller = ConfigurarServidorController()


@router.on_event("startup")
async def start_scheduler():
    return await __controller.configurar_servidor_automaticamente()

