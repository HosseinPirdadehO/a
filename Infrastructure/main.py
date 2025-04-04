import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# مدل‌های Pydantic برای سریال‌سازی داده‌ها


class CategoryBase(BaseModel):
    name: str
    description: str


class BrandBase(BaseModel):
    name: str
    description: str
    image: str  # در اینجا URL تصویر یا مسیر آن را مشخص می‌کنیم


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


class Brand(BrandBase):
    id: int

    class Config:
        from_attributes = True


# پایگاه داده‌ی ساده با استفاده از لیست (برای مثال)
categories_db = []
brands_db = []

# عملیات‌های مربوط به دسته‌بندی


@app.post("/categories/", response_model=Category)
async def create_category(category: CategoryBase):
    new_category = Category(**category.dict(), id=len(categories_db) + 1)
    categories_db.append(new_category)
    return new_category


@app.get("/categories/", response_model=List[Category])
async def get_categories():
    return categories_db


@app.get("/categories/{category_id}", response_model=Category)
async def get_category(category_id: int):
    category = next(
        (cat for cat in categories_db if cat.id == category_id), None)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@app.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, updated_category: CategoryBase):
    category = next(
        (cat for cat in categories_db if cat.id == category_id), None)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category_index = categories_db.index(category)
    categories_db[category_index] = Category(
        **updated_category.dict(), id=category_id)
    return categories_db[category_index]


@app.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    category = next(
        (cat for cat in categories_db if cat.id == category_id), None)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    categories_db.remove(category)
    return {"message": "Category deleted"}

# عملیات‌های مربوط به برند


@app.post("/brands/", response_model=Brand)
async def create_brand(brand: BrandBase):
    new_brand = Brand(**brand.dict(), id=len(brands_db) + 1)
    brands_db.append(new_brand)
    return new_brand


@app.get("/brands/", response_model=List[Brand])
async def get_brands():
    return brands_db


@app.get("/brands/{brand_id}", response_model=Brand)
async def get_brand(brand_id: int):
    brand = next((b for b in brands_db if b.id == brand_id), None)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand


@app.put("/brands/{brand_id}", response_model=Brand)
async def update_brand(brand_id: int, updated_brand: BrandBase):
    brand = next((b for b in brands_db if b.id == brand_id), None)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    brand_index = brands_db.index(brand)
    brands_db[brand_index] = Brand(**updated_brand.dict(), id=brand_id)
    return brands_db[brand_index]


@app.delete("/brands/{brand_id}", response_model=dict)
async def delete_brand(brand_id: int):
    brand = next((b for b in brands_db if b.id == brand_id), None)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    brands_db.remove(brand)
    return {"message": "Brand deleted"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # آدرس اتصال به دیتابیس PostgreSQL
# DATABASE_URL = "postgresql://username:password@localhost/dbname"

# # ایجاد موتور اتصال
# engine = create_engine(DATABASE_URL)

# # ایجاد Session برای ارتباط با دیتابیس
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # پایه‌ی مدل‌های دیتابیس
# Base = declarative_base()
# from sqlalchemy import Column, Integer, String, Text
# from .database import Base

# class Category(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text, nullable=True)

# class Brand(Base):
#     __tablename__ = "brands"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     description = Column(Text, nullable=True)
#     image = Column(String, nullable=True)  # URL تصویر یا مسیر آن
