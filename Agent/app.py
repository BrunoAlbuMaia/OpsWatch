import uvicorn
from decouple import config

if __name__ == '__main__':
    uvicorn.run(app=config("app"), host=config("host"), port=config("port"), log_level="info")
