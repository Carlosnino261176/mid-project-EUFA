from fastapi import FastAPI


app= FastAPI()


@app.get("/")
def inicio():
    return{
        "message":"API EUFA Euro Cup 2020"
    }