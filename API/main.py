from fastapi import FastAPI


app= FastAPI()


Qapp.get("/")
def inicio():
    return{
        "message":"API EUFA Euro Cup 2020"
    }