from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from Application.Controllers import PluginController


router = APIRouter(tags=['Plugin'])
_controller = PluginController()

@router.post("/api/v1/upload", summary="Adiciona um novo plugin ao seu sistema")
async def upload_plugin(hook_file: UploadFile = File(...), plugin_file: UploadFile = File(...)):
    try:
        plugin_filename = plugin_file.filename
        hook_filename = hook_file.filename

        if not plugin_filename.endswith('_plugin.py'):
            raise HTTPException(status_code=400, detail="Nome do arquivo do plugin invalido")
        if not hook_filename.endswith('__hooks.py'):
            raise HTTPException(status_code=400, detail="Nome do arquivo do hooks invalido")
        
        resultado = await _controller.upload_plugin(hook_file, plugin_file)

        return JSONResponse(content=resultado, status_code=200)
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
    

@router.patch("api/v1/update", summary="Atualiza o seu plugin existente, é importante que você envie com o mesmo nome do plugin que deseja alterar")
async def upload_plugin(new_hook_file: UploadFile = File(...), new_plugin_file: UploadFile = File(...)):
    pass