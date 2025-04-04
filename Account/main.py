# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# app = FastAPI()


# class UserBase(BaseModel):
#     first_name: str
#     last_name: str
#     role: str
#     phone_number: str
#     national_id: str
#     province: Optional[int] = None
#     city: Optional[int] = None
#     wallet_status: float
#     messenger: str
#     operations: str
#     status: str


# class UserCreate(UserBase):
#     pass


# class User(UserBase):
#     id: int

#     class Config:
#         from_attributes = True  # تغییر کلید به `from_attributes`


# users_db = []


# @app.post("/users/", response_model=User)
# async def create_user(user: UserCreate):
#     new_user = User(**user.dict(), id=len(users_db) + 1)
#     users_db.append(new_user)
#     return new_user


# @app.get("/users/", response_model=List[User])
# async def read_users():
#     return users_db


# @app.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int):
#     for user in users_db:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=404, detail="User not found")


# @app.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, updated_user: UserCreate):
#     for idx, user in enumerate(users_db):
#         if user.id == user_id:
#             users_db[idx] = User(**updated_user.dict(), id=user.id)
#             return users_db[idx]
#     raise HTTPException(status_code=404, detail="User not found")


# @app.delete("/users/{user_id}", response_model=dict)
# async def delete_user(user_id: int):
#     for idx, user in enumerate(users_db):
#         if user.id == user_id:
#             del users_db[idx]
#             return {"message": "User deleted"}
#
# raise HTTPException(status_code=404, detail="User not found")


# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel, ValidationError
# from typing import List, Optional
# from fastapi.responses import JSONResponse

# router = APIRouter()


# class UserBase(BaseModel):
#     first_name: str
#     last_name: str
#     role: str
#     phone_number: str
#     national_id: str
#     province: Optional[str] = None
#     city: Optional[str] = None
#     wallet_status: float
#     messenger: str
#     operations: str
#     status: str


# class UserCreate(UserBase):
#     pass


# class User(UserBase):
#     id: int

#     class Config:
#         from_attributes = True


# users_db = []


# @router.post("/users/", response_model=User)
# async def create_user(user: UserCreate):
#     try:
#         new_user = User(**user.dict(), id=len(users_db) + 1)
#         users_db.append(new_user)
#         return new_user
#     except ValidationError as e:
#         return JSONResponse(status_code=422, content={"detail": e.errors()})


# @router.get("/users/", response_model=List[User])
# async def read_users():
#     return users_db


# @router.get("/users/{user_id}", response_model=User)
# async def read_user(user_id: int):
#     for user in users_db:
#         if user.id == user_id:
#             return user
#     raise HTTPException(status_code=404, detail="User not found")


# @router.put("/users/{user_id}", response_model=User)
# async def update_user(user_id: int, updated_user: UserCreate):
#     for idx, user in enumerate(users_db):
#         if user.id == user_id:
#             users_db[idx] = User(**updated_user.dict(), id=user.id)
#             return users_db[idx]
#     raise HTTPException(status_code=404, detail="User not found")


# @router.delete("/users/{user_id}", response_model=dict)
# async def delete_user(user_id: int):
#     for idx, user in enumerate(users_db):
#         if user.id == user_id:
#             del users_db[idx]
#             return {"message": "User deleted"}
#     raise HTTPException(status_code=404, detail="User not found")
