import uvicorn


if __name__ == "__main__":
    uvicorn.run('api.app:app', host='0.0.0.0', port=4444, reload=True, lifespan="on")
