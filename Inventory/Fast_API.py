# from fastapi import FastAPI, Depends, HTTPException, Query, Request
# from fastapi.responses import JSONResponse
# from fastapi_jwt_auth import AuthJWT
# from fastapi_jwt_auth.exceptions import AuthJWTException
# from pydantic import BaseModel
# from typing import List, Optional
# from rest_framework.renderers import JSONRenderer
# from django.shortcuts import get_object_or_404
# from django.contrib.auth import authenticate
# from .models import Supplier, InventoryItem, InventoryHistory
# from .Serializers import SupplierSerializer, InventoryItemSerializer, InventoryHistorySerializer

# app = FastAPI()

# # مدل‌های پایدانتیک


# class SupplierPydanticModel(BaseModel):
#     name: str
#     contact_info: str


# class InventoryItemPydanticModel(BaseModel):
#     product: str
#     quantity: int
#     location: str
#     purchase_price: Optional[float] = None
#     expiration_date: Optional[str] = None
#     date_added: str
#     status: str
#     supplier: SupplierPydanticModel

# # مدل پایدانتیک برای ورود به سیستم


# class UserLoginSchema(BaseModel):
#     username: str
#     password: str

# # تنظیمات JWT


# class Settings(BaseModel):
#     authjwt_secret_key: str = "secret"


# @AuthJWT.load_config
# def get_config():
#     return Settings()


# @app.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request: Request, exc: AuthJWTException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.message}
#     )

# # تابع احراز هویت


# def authenticate_user(username: str, password: str):
#     user = authenticate(username=username, password=password)
#     if not user:
#         return None
#     return user

# # ورود به سیستم


# @app.post('/login/')
# def login(user: UserLoginSchema, Authorize: AuthJWT = Depends()):
#     user = authenticate_user(user.username, user.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Bad username or password")

#     access_token = Authorize.create_access_token(subject=user.username)
#     return {"access_token": access_token}


# @app.get("/protected/", dependencies=[Depends(AuthJWT().jwt_required)])
# def protected(Authorize: AuthJWT = Depends()):
#     Authorize.jwt_required()
#     return {"message": "You are logged in!"}

# # عملیات CRUD


# @app.post("/suppliers/", response_model=SupplierPydanticModel)
# def create_supplier(supplier: SupplierPydanticModel):
#     supplier_instance = Supplier.objects.create(**supplier.dict())
#     serializer = SupplierSerializer(supplier_instance)
#     return JSONRenderer().render(serializer.data)


# @app.get("/suppliers/", response_model=List[SupplierPydanticModel])
# def get_suppliers():
#     suppliers = Supplier.objects.all()
#     serializer = SupplierSerializer(suppliers, many=True)
#     return JSONRenderer().render(serializer.data)


# @app.get("/suppliers/{supplier_id}/", response_model=SupplierPydanticModel)
# def get_supplier(supplier_id: int):
#     supplier = get_object_or_404(Supplier, id=supplier_id)
#     serializer = SupplierSerializer(supplier)
#     return JSONRenderer().render(serializer.data)


# @app.put("/suppliers/{supplier_id}/", response_model=SupplierPydanticModel)
# def update_supplier(supplier_id: int, updated_supplier: SupplierPydanticModel):
#     supplier = get_object_or_404(Supplier, id=supplier_id)
#     for key, value in updated_supplier.dict().items():
#         setattr(supplier, key, value)
#     supplier.save()
#     serializer = SupplierSerializer(supplier)
#     return JSONRenderer().render(serializer.data)


# @app.delete("/suppliers/{supplier_id}/")
# def delete_supplier(supplier_id: int):
#     supplier = get_object_or_404(Supplier, id=supplier_id)
#     supplier.delete()
#     return {"message": "Supplier deleted successfully"}


# @app.post("/inventory_items/", response_model=InventoryItemPydanticModel)
# def create_inventory_item(item: InventoryItemPydanticModel):
#     item_instance = InventoryItem.objects.create(**item.dict())
#     serializer = InventoryItemSerializer(item_instance)
#     return JSONRenderer().render(serializer.data)


# @app.get("/inventory_items/", response_model=List[InventoryItemPydanticModel])
# def get_inventory_items(
#     status: Optional[str] = Query(
#         None, description="Status of inventory items"),
#     location: Optional[str] = Query(
#         None, description="Location of inventory items")
# ):
#     items = InventoryItem.objects.all()
#     if status:
#         items = items.filter(status=status)
#     if location:
#         items = items.filter(location=location)
#     serializer = InventoryItemSerializer(items, many=True)
#     return JSONRenderer().render(serializer.data)


# @app.get("/inventory_items/{item_id}/", response_model=InventoryItemPydanticModel)
# def get_inventory_item(item_id: int):
#     item = get_object_or_404(InventoryItem, id=item_id)
#     serializer = InventoryItemSerializer(item)
#     return JSONRenderer().render(serializer.data)


# @app.put("/inventory_items/{item_id}/", response_model=InventoryItemPydanticModel)
# def update_inventory_item(item_id: int, updated_item: InventoryItemPydanticModel):
#     item = get_object_or_404(InventoryItem, id=item_id)
#     for key, value in updated_item.dict().items():
#         setattr(item, key, value)
#     item.save()
#     serializer = InventoryItemSerializer(item)
#     return JSONRenderer().render(serializer.data)


# @app.delete("/inventory_items/{item_id}/")
# def delete_inventory_item(item_id: int):
#     item = get_object_or_404(InventoryItem, id=item_id)
#     item.delete()
#     return {"message": "Inventory item deleted successfully"}
