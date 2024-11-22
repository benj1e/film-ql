from fastapi import FastAPI

from .routers.tmdb_router import router

app = FastAPI()


@app.get("/", status_code=418)
async def index():
    return {"message": "Hello World"}


app.include_router(router)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
