import uvicorn
from decouple import config
from src import app

if __name__ == '__main__':
    uvicorn.run(app=app, host=config("host"), port=config("port"))
                # log_level="info")
