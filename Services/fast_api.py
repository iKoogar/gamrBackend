from fastapi import FastAPI
import Services.data_service as svc


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/newUserTest/{name}")
async def newUser(nam: str):
    svc.addUser(nam, "noemail", "nopwd")

@app.get("/allUsers")
async def getAllUsers():
    return svc.getAllUsers()