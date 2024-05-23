from fastapi import APIRouter, UploadFile, File
import os
import shutil


router = APIRouter(tags=['Plugin'])


@router.post("/upload-plugin/")
async def upload_plugin(file: UploadFile = File(...)):
    plugin_directory = 'Infrastructure/CrossCutting/plugins/plugins'
    plugin_path = os.path.join(plugin_directory, file.filename)
    with open(plugin_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Recarregar plugins após upload
    # job_service.plugin_manager.load_plugins()
    return {"message": "Plugin uploaded and loaded successfully"}

# @router.get("/execute-job")
# async def execute_job():
#     try:
#         configDetalhes = {
#             # Exemplo de configuração detalhada
#         }
#         plugin_manager.execute_plugins('on_pre_exec', configDetalhes)
#         # Lógica de execução do trabalho principal
#         plugin_manager.execute_plugins('on_post_exec', configDetalhes)
#         return {"message": "Job executado com sucesso"}
#     except Exception as ex:
#         return {"error": str(ex)}
