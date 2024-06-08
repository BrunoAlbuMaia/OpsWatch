import uvicorn
from Application.main import app

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=9002, log_level="info")
