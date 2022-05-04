from fastapi import FastAPI
import uvicorn
import settings

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():

    uvicorn.run(
        "main:app",
        host=settings.SERVICE_HOST,
        port=int(settings.SERVICE_PORT),
        workers=int(settings.WORKERS_AMOUNT)
    )

if __name__ == '__main__':
    main()
