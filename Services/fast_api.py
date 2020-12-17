"""
fast_api.py
creates the fastAPI app
contains the endpoints for our API
"""

from fastapi import FastAPI
import Services.data_service as svc


app = FastAPI()

# root
@app.get("/")
async def root():
    return {"message": "Hello World"}

# tests inserting a user to the database
@app.post("/newUserTest/{name}")
async def newUser(nam: str):
    svc.addUser(nam, "noemail", "nopwd")

# returns all users in the database
@app.get("/allUsers")
async def getAllUsers():
    return svc.getAllUsers()

# returns the user with the specified email
@app.get("/userByEmail/{usr}")
async def userByEmail(usr):
    return svc.findUserByEmail(usr).to_json()
