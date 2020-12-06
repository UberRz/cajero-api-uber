''' from db import user_db

def main():
    print("db:\n")
    print(user_db.database_users)
    print("camilo:\n")
    print(user_db.get_user("camilo24"))


if __name__== '__main__':
    main() '''

from fastapi import FastAPI
from db.user_db import database_users
from fastapi import HTTPException
from db.user_db import UserInDB

app=FastAPI()

@app.get("/")                   #GET / HTTP/1.1 (lado del cliente)
async def root():
    return {"message": "Hello FastAPI"} 

@app.get("/users")               #GET /users  HTTP/1.1 (lado del cliente)
async def users():
    return {"message": database_users}

@app.get("/users/{username}")               #GET /users/username HTTP/1.1 (lado del cliente)
async def get_user_by_username(username:str):
    if username in database_users:
        return {"message": database_users[username]}
#    return {"message": "Usuario no encontrado"}
    raise HTTPException(status_code=404, detail="El usuario no existe")    

@app.post("/users/")
async def create_user(user: UserInDB):
    database_users[user.username]=user
    return user

@app.delete("/users/")
async def create_user(user : UserInDB):
    del database_users[user.username] 
    return user

@app.put("/users/")
async def create_user(user : UserInDB):
    database_users[user.username] = user 
    return user

