from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Float
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError
from typing import List, Optional


# app Account

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class UserBase(BaseModel):
    first_name: str
    last_name: str
    role: str
    phone_number: str
    national_id: str
    province: Optional[str] = None
    city: Optional[str] = None
    wallet_status: float
    messenger: str
    operations: str
    status: str
    created_at: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
users_db = []

# عملیات CRUD


@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    try:
        print("Received user data:", user.dict())
        new_user = User(**user.dict(), id=len(users_db) + 1,
                        created_at="2025-04-04")  # تاریخ نمونه
        users_db.append(new_user)
        return new_user
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 10):
    return users_db[skip:skip + limit]


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, updated_user: UserCreate):
    user = next((u for u in users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_index = users_db.index(user)
    users_db[user_index] = User(
        **updated_user.dict(), id=user_id, created_at=user.created_at)
    return users_db[user_index]


@router.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    user = next((u for u in users_db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.remove(user)
    return {"message": "User deleted"}

app.include_router(router, prefix="/user_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /user_api/users/     - ایجاد کاربر جدید
# GET    /user_api/users/     - دریافت لیست کاربران
# GET    /user_api/users/{id} - دریافت جزئیات یک کاربر
# PUT    /user_api/users/{id} - بروزرسانی اطلاعات یک کاربر
# DELETE /user_api/users/{id} - حذف یک کاربر

#

#

#

#

#

#

# app Infrastucture

# category

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
categories_db = []

# عملیات CRUD


@router.post("/categories/", response_model=Category)
async def create_category(category: CategoryCreate):
    try:
        print("Received category data:", category.dict())
        new_category = Category(**category.dict(), id=len(categories_db) + 1)
        categories_db.append(new_category)
        return new_category
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/categories/", response_model=List[Category])
async def read_categories(skip: int = 0, limit: int = 10):
    return categories_db[skip:skip + limit]


@router.get("/categories/{category_id}", response_model=Category)
async def read_category(category_id: int):
    category = next(
        (cat for cat in categories_db if cat.id == category_id), None)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/categories/{category_id}", response_model=Category)
async def update_category(category_id: int, updated_category: CategoryCreate):
    category = next(
        (cat for cat in categories_db if cat.id == category_id), None)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    category_index = categories_db.index(category)
    categories_db[category_index] = Category(
        **updated_category.dict(), id=category_id)
    return categories_db[category_index]


@router.delete("/categories/{category_id}", response_model=dict)
async def delete_category(category_id: int):
    category = next(
        (cat for cat in categories_db if cat.id == category_id), None)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    categories_db.remove(category)
    return {"message": "Category deleted"}

app.include_router(router, prefix="/category_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /category_api/categories/     - ایجاد دسته‌بندی جدید
# GET    /category_api/categories/     - دریافت لیست دسته‌بندی‌ها
# GET    /category_api/categories/{id} - دریافت جزئیات یک دسته‌بندی خاص
# PUT    /category_api/categories/{id} - بروزرسانی اطلاعات یک دسته‌بندی
# DELETE /category_api/categories/{id} - حذف یک دسته‌بندی


# Brand

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class BrandBase(BaseModel):
    name: str
    description: str
    image: Optional[str] = None  # مسیر آپلود تصویر برند


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
brands_db = []

# عملیات CRUD


@router.post("/brands/", response_model=Brand)
async def create_brand(brand: BrandCreate):
    try:
        print("Received brand data:", brand.dict())
        new_brand = Brand(**brand.dict(), id=len(brands_db) + 1)
        brands_db.append(new_brand)
        return new_brand
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/brands/", response_model=List[Brand])
async def read_brands(skip: int = 0, limit: int = 10):
    return brands_db[skip:skip + limit]


@router.get("/brands/{brand_id}", response_model=Brand)
async def read_brand(brand_id: int):
    brand = next((b for b in brands_db if b.id == brand_id), None)
    if brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand


@router.put("/brands/{brand_id}", response_model=Brand)
async def update_brand(brand_id: int, updated_brand: BrandCreate):
    brand = next((b for b in brands_db if b.id == brand_id), None)
    if brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    brand_index = brands_db.index(brand)
    brands_db[brand_index] = Brand(**updated_brand.dict(), id=brand_id)
    return brands_db[brand_index]


@router.delete("/brands/{brand_id}", response_model=dict)
async def delete_brand(brand_id: int):
    brand = next((b for b in brands_db if b.id == brand_id), None)
    if brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    brands_db.remove(brand)
    return {"message": "Brand deleted"}

app.include_router(router, prefix="/brand_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /brand_api/brands/     - ایجاد برند جدید
# GET    /brand_api/brands/     - دریافت لیست برندها
# GET    /brand_api/brands/{id} - دریافت جزئیات یک برند خاص
# PUT    /brand_api/brands/{id} - بروزرسانی اطلاعات یک برند
# DELETE /brand_api/brands/{id} - حذف یک برند

#

#

#

#

#

#

#

#

#

#

#

# app Inventory
# Inventory
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()


class InventoryBase(BaseModel):
    image: Optional[str] = None
    product_name: str
    stock: int
    unit: str
    stock_alert: bool = False
    category: str
    brand: str
    purchase_price: float
    cover_price: float
    sale_price: float
    manufacture_date: Optional[str] = None
    expiry_date: Optional[str] = None
    expiry_threshold: Optional[int] = None
    sale_status: str
    sale_range: Optional[str] = None
    marketer_profit: Optional[float] = None
    turnover: Optional[float] = None
    operations: Optional[str] = None
    description: Optional[str] = None


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    id: int

    class Config:
        from_attributes = True


inventories_db = []


@router.post("/inventories/", response_model=Inventory)
async def create_inventory(inventory: InventoryCreate):
    try:
        print("Received inventory data:", inventory.dict())
        new_inventory = Inventory(
            **inventory.dict(), id=len(inventories_db) + 1)
        inventories_db.append(new_inventory)
        return new_inventory
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/inventories/", response_model=List[Inventory])
async def read_inventories(skip: int = 0, limit: int = 10):
    return inventories_db[skip:skip + limit]


@router.get("/inventories/{inventory_id}", response_model=Inventory)
async def read_inventory(inventory_id: int):
    inventory = next(
        (inv for inv in inventories_db if inv.id == inventory_id), None)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inventory


@router.put("/inventories/{inventory_id}", response_model=Inventory)
async def update_inventory(inventory_id: int, updated_inventory: InventoryCreate):
    inventory = next(
        (inv for inv in inventories_db if inv.id == inventory_id), None)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory_index = inventories_db.index(inventory)
    inventories_db[inventory_index] = Inventory(
        **updated_inventory.dict(), id=inventory_id)
    return inventories_db[inventory_index]


@router.delete("/inventories/{inventory_id}", response_model=dict)
async def delete_inventory(inventory_id: int):
    inventory = next(
        (inv for inv in inventories_db if inv.id == inventory_id), None)
    if inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventories_db.remove(inventory)
    return {"message": "Inventory deleted"}

app.include_router(router, prefix="/inventory_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# آدرس ها http://127.0.0.1:8000/inventory_api/inventories/
# آدرس ها http://127.0.0.1:8000/inventory_api/inventories/id put delete


#

#

#

#

#

#

#

#

#

#

#

# app Notif
# NotificationSms

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class NotificationSmsBase(BaseModel):
    title: str
    content: str
    city: str
    user_group: str
    is_selected: bool = False
    action: Optional[str] = None


class NotificationSmsCreate(NotificationSmsBase):
    pass


class NotificationSms(NotificationSmsBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
notifications_db = []

# عملیات CRUD


@router.post("/notifications/", response_model=NotificationSms)
async def create_notification(notification: NotificationSmsCreate):
    try:
        print("Received notification data:", notification.dict())
        new_notification = NotificationSms(
            **notification.dict(), id=len(notifications_db) + 1
        )
        notifications_db.append(new_notification)
        return new_notification
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/notifications/", response_model=List[NotificationSms])
async def read_notifications(skip: int = 0, limit: int = 10):
    return notifications_db[skip:skip + limit]


@router.get("/notifications/{notification_id}", response_model=NotificationSms)
async def read_notification(notification_id: int):
    notification = next(
        (notif for notif in notifications_db if notif.id == notification_id), None
    )
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification


@router.put("/notifications/{notification_id}", response_model=NotificationSms)
async def update_notification(
    notification_id: int, updated_notification: NotificationSmsCreate
):
    notification = next(
        (notif for notif in notifications_db if notif.id == notification_id), None
    )
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    notification_index = notifications_db.index(notification)
    notifications_db[notification_index] = NotificationSms(
        **updated_notification.dict(), id=notification_id
    )
    return notifications_db[notification_index]


@router.delete("/notifications/{notification_id}", response_model=dict)
async def delete_notification(notification_id: int):
    notification = next(
        (notif for notif in notifications_db if notif.id == notification_id), None
    )
    if notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    notifications_db.remove(notification)
    return {"message": "Notification deleted"}

app.include_router(router, prefix="/notification_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /notification_api/notifications/     - ایجاد پیامک اطلاع‌رسانی جدید
# GET    /notification_api/notifications/     - دریافت لیست پیامک‌ها
# GET    /notification_api/notifications/{id} - دریافت جزئیات یک پیامک
# PUT    /notification_api/notifications/{id} - بروزرسانی اطلاعات پیامک
# DELETE /notification_api/notifications/{id} - حذف پیامک اطلاع‌رسانی


# ModalNotification

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class ModalNotificationBase(BaseModel):
    image: Optional[str] = None  # مسیر آپلود تصویر
    link: Optional[str] = None  # لینک مرتبط با اطلاع‌رسانی
    content: str
    province: str
    city: str
    individual: Optional[str] = None  # فرد مورد نظر
    user_group: str
    action: Optional[str] = None


class ModalNotificationCreate(ModalNotificationBase):
    pass


class ModalNotification(ModalNotificationBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
modal_notifications_db = []

# عملیات CRUD


@router.post("/modal_notifications/", response_model=ModalNotification)
async def create_modal_notification(modal_notification: ModalNotificationCreate):
    try:
        print("Received modal notification data:", modal_notification.dict())
        new_notification = ModalNotification(
            **modal_notification.dict(), id=len(modal_notifications_db) + 1
        )
        modal_notifications_db.append(new_notification)
        return new_notification
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/modal_notifications/", response_model=List[ModalNotification])
async def read_modal_notifications(skip: int = 0, limit: int = 10):
    return modal_notifications_db[skip:skip + limit]


@router.get("/modal_notifications/{notification_id}", response_model=ModalNotification)
async def read_modal_notification(notification_id: int):
    modal_notification = next(
        (notif for notif in modal_notifications_db if notif.id == notification_id), None
    )
    if modal_notification is None:
        raise HTTPException(
            status_code=404, detail="Modal notification not found")
    return modal_notification


@router.put("/modal_notifications/{notification_id}", response_model=ModalNotification)
async def update_modal_notification(
    notification_id: int, updated_notification: ModalNotificationCreate
):
    modal_notification = next(
        (notif for notif in modal_notifications_db if notif.id == notification_id), None
    )
    if modal_notification is None:
        raise HTTPException(
            status_code=404, detail="Modal notification not found")
    notification_index = modal_notifications_db.index(modal_notification)
    modal_notifications_db[notification_index] = ModalNotification(
        **updated_notification.dict(), id=notification_id
    )
    return modal_notifications_db[notification_index]


@router.delete("/modal_notifications/{notification_id}", response_model=dict)
async def delete_modal_notification(notification_id: int):
    modal_notification = next(
        (notif for notif in modal_notifications_db if notif.id == notification_id), None
    )
    if modal_notification is None:
        raise HTTPException(
            status_code=404, detail="Modal notification not found")
    modal_notifications_db.remove(modal_notification)
    return {"message": "Modal notification deleted"}

app.include_router(router, prefix="/modal_notification_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /modal_notification_api/modal_notifications/     - ایجاد اطلاع‌رسانی مودال جدید
# GET    /modal_notification_api/modal_notifications/     - دریافت لیست اطلاع‌رسانی‌های مودال
# GET    /modal_notification_api/modal_notifications/{id} - دریافت جزئیات یک اطلاع‌رسانی مودال
# PUT    /modal_notification_api/modal_notifications/{id} - بروزرسانی یک اطلاع‌رسانی مودال
# DELETE /modal_notification_api/modal_notifications/{id} - حذف اطلاع‌رسانی مودال


# ContentNotification

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class ContentNotificationBase(BaseModel):
    image: Optional[str] = None  # مسیر آپلود تصویر
    link: Optional[str] = None  # لینک مرتبط با اطلاع‌رسانی
    content: str
    province: str
    city: str
    individual: Optional[str] = None  # فرد مشخص‌شده
    user_group: str
    action: Optional[str] = None


class ContentNotificationCreate(ContentNotificationBase):
    pass


class ContentNotification(ContentNotificationBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
content_notifications_db = []

# عملیات CRUD


@router.post("/content_notifications/", response_model=ContentNotification)
async def create_content_notification(content_notification: ContentNotificationCreate):
    try:
        print("Received content notification data:",
              content_notification.dict())
        new_notification = ContentNotification(
            **content_notification.dict(), id=len(content_notifications_db) + 1
        )
        content_notifications_db.append(new_notification)
        return new_notification
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/content_notifications/", response_model=List[ContentNotification])
async def read_content_notifications(skip: int = 0, limit: int = 10):
    return content_notifications_db[skip:skip + limit]


@router.get("/content_notifications/{notification_id}", response_model=ContentNotification)
async def read_content_notification(notification_id: int):
    content_notification = next(
        (notif for notif in content_notifications_db if notif.id == notification_id), None
    )
    if content_notification is None:
        raise HTTPException(
            status_code=404, detail="Content notification not found")
    return content_notification


@router.put("/content_notifications/{notification_id}", response_model=ContentNotification)
async def update_content_notification(
    notification_id: int, updated_notification: ContentNotificationCreate
):
    content_notification = next(
        (notif for notif in content_notifications_db if notif.id == notification_id), None
    )
    if content_notification is None:
        raise HTTPException(
            status_code=404, detail="Content notification not found")
    notification_index = content_notifications_db.index(content_notification)
    content_notifications_db[notification_index] = ContentNotification(
        **updated_notification.dict(), id=notification_id
    )
    return content_notifications_db[notification_index]


@router.delete("/content_notifications/{notification_id}", response_model=dict)
async def delete_content_notification(notification_id: int):
    content_notification = next(
        (notif for notif in content_notifications_db if notif.id == notification_id), None
    )
    if content_notification is None:
        raise HTTPException(
            status_code=404, detail="Content notification not found")
    content_notifications_db.remove(content_notification)
    return {"message": "Content notification deleted"}

app.include_router(router, prefix="/content_notification_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /content_notification_api/content_notifications/     - ایجاد اطلاع‌رسانی جدید
# GET    /content_notification_api/content_notifications/     - دریافت لیست اطلاع‌رسانی‌ها
# GET    /content_notification_api/content_notifications/{id} - دریافت جزئیات یک اطلاع‌رسانی
# PUT    /content_notification_api/content_notifications/{id} - بروزرسانی یک اطلاع‌رسانی
# DELETE /content_notification_api/content_notifications/{id} - حذف یک اطلاع‌رسانی


# AdvertisementNotification


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class AdvertisementNotificationBase(BaseModel):
    image: Optional[str] = None  # مسیر آپلود تصویر
    link: Optional[str] = None  # لینک مرتبط با اطلاع‌رسانی
    content: str
    province: str
    city: str
    individual: Optional[str] = None  # فرد مشخص‌شده
    user_group: str
    action: Optional[str] = None


class AdvertisementNotificationCreate(AdvertisementNotificationBase):
    pass


class AdvertisementNotification(AdvertisementNotificationBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
advertisement_notifications_db = []

# عملیات CRUD


@router.post("/advertisement_notifications/", response_model=AdvertisementNotification)
async def create_advertisement_notification(advertisement_notification: AdvertisementNotificationCreate):
    try:
        print("Received advertisement notification data:",
              advertisement_notification.dict())
        new_notification = AdvertisementNotification(
            **advertisement_notification.dict(), id=len(advertisement_notifications_db) + 1
        )
        advertisement_notifications_db.append(new_notification)
        return new_notification
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/advertisement_notifications/", response_model=List[AdvertisementNotification])
async def read_advertisement_notifications(skip: int = 0, limit: int = 10):
    return advertisement_notifications_db[skip:skip + limit]


@router.get("/advertisement_notifications/{notification_id}", response_model=AdvertisementNotification)
async def read_advertisement_notification(notification_id: int):
    advertisement_notification = next(
        (notif for notif in advertisement_notifications_db if notif.id ==
         notification_id), None
    )
    if advertisement_notification is None:
        raise HTTPException(
            status_code=404, detail="Advertisement notification not found")
    return advertisement_notification


@router.put("/advertisement_notifications/{notification_id}", response_model=AdvertisementNotification)
async def update_advertisement_notification(
    notification_id: int, updated_notification: AdvertisementNotificationCreate
):
    advertisement_notification = next(
        (notif for notif in advertisement_notifications_db if notif.id ==
         notification_id), None
    )
    if advertisement_notification is None:
        raise HTTPException(
            status_code=404, detail="Advertisement notification not found")
    notification_index = advertisement_notifications_db.index(
        advertisement_notification)
    advertisement_notifications_db[notification_index] = AdvertisementNotification(
        **updated_notification.dict(), id=notification_id
    )
    return advertisement_notifications_db[notification_index]


@router.delete("/advertisement_notifications/{notification_id}", response_model=dict)
async def delete_advertisement_notification(notification_id: int):
    advertisement_notification = next(
        (notif for notif in advertisement_notifications_db if notif.id ==
         notification_id), None
    )
    if advertisement_notification is None:
        raise HTTPException(
            status_code=404, detail="Advertisement notification not found")
    advertisement_notifications_db.remove(advertisement_notification)
    return {"message": "Advertisement notification deleted"}

app.include_router(router, prefix="/advertisement_notification_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /advertisement_notification_api/advertisement_notifications/     - ایجاد اطلاع‌رسانی تبلیغاتی جدید
# GET    /advertisement_notification_api/advertisement_notifications/     - دریافت لیست اطلاع‌رسانی‌های تبلیغاتی
# GET    /advertisement_notification_api/advertisement_notifications/{id} - دریافت جزئیات یک اطلاع‌رسانی تبلیغاتی
# PUT    /advertisement_notification_api/advertisement_notifications/{id} - بروزرسانی یک اطلاع‌رسانی تبلیغاتی
# DELETE /advertisement_notification_api/advertisement_notifications/{id} - حذف یک اطلاع‌رسانی تبلیغاتی


#

#

#

#

#

#

#

#

#

#

#

# app Shopper
# Shopper

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models برای داده‌های ورودی و خروجی


class ShopperBase(BaseModel):
    full_name: str
    store_name: str
    contact_number: str
    national_code: str
    status: str
    province: str
    city: str
    location: str
    shopping_cart: Optional[str] = None
    financial_limit: float = 0.0
    history: Optional[str] = None
    notifications: Optional[str] = None
    is_authenticated: bool = False
    actions: Optional[str] = None


class ShopperCreate(ShopperBase):
    pass


class Shopper(ShopperBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت (لیست)
shoppers_db = []

# متدهای CRUD برای Shopper


@router.post("/shoppers/", response_model=Shopper)
async def create_shopper(shopper: ShopperCreate):
    try:
        print("Received shopper data:", shopper.dict())
        new_shopper = Shopper(**shopper.dict(), id=len(shoppers_db) + 1)
        shoppers_db.append(new_shopper)
        return new_shopper
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/shoppers/", response_model=List[Shopper])
async def read_shoppers(skip: int = 0, limit: int = 10):
    return shoppers_db[skip:skip + limit]


@router.get("/shoppers/{shopper_id}", response_model=Shopper)
async def read_shopper(shopper_id: int):
    shopper = next((s for s in shoppers_db if s.id == shopper_id), None)
    if shopper is None:
        raise HTTPException(status_code=404, detail="Shopper not found")
    return shopper


@router.put("/shoppers/{shopper_id}", response_model=Shopper)
async def update_shopper(shopper_id: int, updated_shopper: ShopperCreate):
    shopper = next((s for s in shoppers_db if s.id == shopper_id), None)
    if shopper is None:
        raise HTTPException(status_code=404, detail="Shopper not found")
    shopper_index = shoppers_db.index(shopper)
    shoppers_db[shopper_index] = Shopper(
        **updated_shopper.dict(), id=shopper_id)
    return shoppers_db[shopper_index]


@router.delete("/shoppers/{shopper_id}", response_model=dict)
async def delete_shopper(shopper_id: int):
    shopper = next((s for s in shoppers_db if s.id == shopper_id), None)
    if shopper is None:
        raise HTTPException(status_code=404, detail="Shopper not found")
    shoppers_db.remove(shopper)
    return {"message": "Shopper deleted"}

app.include_router(router, prefix="/shopper_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /shopper_api/shoppers/         - ایجاد خریدار جدید
# GET    /shopper_api/shoppers/         - دریافت لیست خریداران
# GET    /shopper_api/shoppers/{id}     - دریافت جزئیات یک خریدار
# PUT    /shopper_api/shoppers/{id}     - بروزرسانی اطلاعات یک خریدار
# DELETE /shopper_api/shoppers/{id}     - حذف یک خریدار


# Buyer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class BuyerBase(BaseModel):
    first_name: str
    last_name: str
    store_name: str
    phone_number: str
    national_id: str
    status: str
    province: Optional[str] = None
    city: Optional[str] = None
    shopping_cart: Optional[str] = None
    financial_limit: str
    purchase_history: Optional[str] = None
    messenger: str
    authentication: bool = False
    operations: str
    current_location: Optional[str] = None


class BuyerCreate(BuyerBase):
    pass


class Buyer(BuyerBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
buyers_db = []

# متدهای CRUD


@router.post("/buyers/", response_model=Buyer)
async def create_buyer(buyer: BuyerCreate):
    try:
        print("Received buyer data:", buyer.dict())
        new_buyer = Buyer(**buyer.dict(), id=len(buyers_db) + 1)
        buyers_db.append(new_buyer)
        return new_buyer
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/buyers/", response_model=List[Buyer])
async def read_buyers(skip: int = 0, limit: int = 10):
    return buyers_db[skip:skip + limit]


@router.get("/buyers/{buyer_id}", response_model=Buyer)
async def read_buyer(buyer_id: int):
    buyer = next((b for b in buyers_db if b.id == buyer_id), None)
    if buyer is None:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return buyer


@router.put("/buyers/{buyer_id}", response_model=Buyer)
async def update_buyer(buyer_id: int, updated_buyer: BuyerCreate):
    buyer = next((b for b in buyers_db if b.id == buyer_id), None)
    if buyer is None:
        raise HTTPException(status_code=404, detail="Buyer not found")
    buyer_index = buyers_db.index(buyer)
    buyers_db[buyer_index] = Buyer(**updated_buyer.dict(), id=buyer_id)
    return buyers_db[buyer_index]


@router.delete("/buyers/{buyer_id}", response_model=dict)
async def delete_buyer(buyer_id: int):
    buyer = next((b for b in buyers_db if b.id == buyer_id), None)
    if buyer is None:
        raise HTTPException(status_code=404, detail="Buyer not found")
    buyers_db.remove(buyer)
    return {"message": "Buyer deleted"}

app.include_router(router, prefix="/buyer_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /buyer_api/buyers/             - ایجاد خریدار جدید
# GET    /buyer_api/buyers/             - دریافت لیست خریداران
# GET    /buyer_api/buyers/{id}         - دریافت جزئیات یک خریدار
# PUT    /buyer_api/buyers/{id}         - بروزرسانی اطلاعات یک خریدار
# DELETE /buyer_api/buyers/{id}         - حذف یک خریدار


# BuyerCart

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models برای داده‌های ورودی و خروجی


class BuyerCartBase(BaseModel):
    order_number: str
    purchase_type: str
    order_date: str  # DateTime به صورت رشته در Pydantic
    delivery_date: str  # DateTime به صورت رشته در Pydantic
    total_amount: float
    settlement_type: str
    product_name: str
    quantity: int
    unit_price: float


class BuyerCartCreate(BuyerCartBase):
    pass


class BuyerCart(BuyerCartBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
buyer_carts_db = []

# عملیات CRUD


@router.post("/buyer_carts/", response_model=BuyerCart)
async def create_buyer_cart(buyer_cart: BuyerCartCreate):
    try:
        print("Received buyer cart data:", buyer_cart.dict())
        new_buyer_cart = BuyerCart(
            **buyer_cart.dict(), id=len(buyer_carts_db) + 1)
        buyer_carts_db.append(new_buyer_cart)
        return new_buyer_cart
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/buyer_carts/", response_model=List[BuyerCart])
async def read_buyer_carts(skip: int = 0, limit: int = 10):
    return buyer_carts_db[skip:skip + limit]


@router.get("/buyer_carts/{buyer_cart_id}", response_model=BuyerCart)
async def read_buyer_cart(buyer_cart_id: int):
    buyer_cart = next(
        (cart for cart in buyer_carts_db if cart.id == buyer_cart_id), None)
    if buyer_cart is None:
        raise HTTPException(status_code=404, detail="Buyer cart not found")
    return buyer_cart


@router.put("/buyer_carts/{buyer_cart_id}", response_model=BuyerCart)
async def update_buyer_cart(buyer_cart_id: int, updated_buyer_cart: BuyerCartCreate):
    buyer_cart = next(
        (cart for cart in buyer_carts_db if cart.id == buyer_cart_id), None)
    if buyer_cart is None:
        raise HTTPException(status_code=404, detail="Buyer cart not found")
    buyer_cart_index = buyer_carts_db.index(buyer_cart)
    buyer_carts_db[buyer_cart_index] = BuyerCart(
        **updated_buyer_cart.dict(), id=buyer_cart_id)
    return buyer_carts_db[buyer_cart_index]


@router.delete("/buyer_carts/{buyer_cart_id}", response_model=dict)
async def delete_buyer_cart(buyer_cart_id: int):
    buyer_cart = next(
        (cart for cart in buyer_carts_db if cart.id == buyer_cart_id), None)
    if buyer_cart is None:
        raise HTTPException(status_code=404, detail="Buyer cart not found")
    buyer_carts_db.remove(buyer_cart)
    return {"message": "Buyer cart deleted"}

app.include_router(router, prefix="/buyer_cart_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# BuyerProduct

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class BuyerProductBase(BaseModel):
    cart_id: int  # ارجاع به ID سبد خرید
    product_name: str
    quantity: int
    unit_price: float


class BuyerProductCreate(BuyerProductBase):
    pass


class BuyerProduct(BuyerProductBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
buyer_products_db = []

# عملیات CRUD


@router.post("/buyer_products/", response_model=BuyerProduct)
async def create_buyer_product(buyer_product: BuyerProductCreate):
    try:
        print("Received buyer product data:", buyer_product.dict())
        new_buyer_product = BuyerProduct(
            **buyer_product.dict(), id=len(buyer_products_db) + 1)
        buyer_products_db.append(new_buyer_product)
        return new_buyer_product
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/buyer_products/", response_model=List[BuyerProduct])
async def read_buyer_products(skip: int = 0, limit: int = 10):
    return buyer_products_db[skip:skip + limit]


@router.get("/buyer_products/{buyer_product_id}", response_model=BuyerProduct)
async def read_buyer_product(buyer_product_id: int):
    buyer_product = next(
        (prod for prod in buyer_products_db if prod.id == buyer_product_id), None)
    if buyer_product is None:
        raise HTTPException(status_code=404, detail="Buyer product not found")
    return buyer_product


@router.put("/buyer_products/{buyer_product_id}", response_model=BuyerProduct)
async def update_buyer_product(buyer_product_id: int, updated_buyer_product: BuyerProductCreate):
    buyer_product = next(
        (prod for prod in buyer_products_db if prod.id == buyer_product_id), None)
    if buyer_product is None:
        raise HTTPException(status_code=404, detail="Buyer product not found")
    buyer_product_index = buyer_products_db.index(buyer_product)
    buyer_products_db[buyer_product_index] = BuyerProduct(
        **updated_buyer_product.dict(), id=buyer_product_id)
    return buyer_products_db[buyer_product_index]


@router.delete("/buyer_products/{buyer_product_id}", response_model=dict)
async def delete_buyer_product(buyer_product_id: int):
    buyer_product = next(
        (prod for prod in buyer_products_db if prod.id == buyer_product_id), None)
    if buyer_product is None:
        raise HTTPException(status_code=404, detail="Buyer product not found")
    buyer_products_db.remove(buyer_product)
    return {"message": "Buyer product deleted"}

app.include_router(router, prefix="/buyer_product_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /buyer_cart_api/buyer_carts/   - ایجاد سبد خرید جدید
# GET    /buyer_cart_api/buyer_carts/   - دریافت لیست سبدهای خرید
# GET    /buyer_cart_api/buyer_carts/{id} - دریافت جزئیات یک سبد خرید
# PUT    /buyer_cart_api/buyer_carts/{id} - بروزرسانی اطلاعات یک سبد خرید
# DELETE /buyer_cart_api/buyer_carts/{id} - حذف یک سبد خرید


# PurchaseHistory

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class PurchaseHistoryBase(BaseModel):
    contact_number: str
    purchase_type: str
    order_date: str  # تاریخ سفارش به صورت رشته
    delivery_date: str  # تاریخ تحویل به صورت رشته
    settlement_date: str  # تاریخ تسویه حساب به صورت رشته
    settlement_details: str


class PurchaseHistoryCreate(PurchaseHistoryBase):
    pass


class PurchaseHistory(PurchaseHistoryBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
purchase_histories_db = []

# عملیات CRUD


@router.post("/purchase_histories/", response_model=PurchaseHistory)
async def create_purchase_history(purchase_history: PurchaseHistoryCreate):
    try:
        print("Received purchase history data:", purchase_history.dict())
        new_purchase_history = PurchaseHistory(
            **purchase_history.dict(), id=len(purchase_histories_db) + 1
        )
        purchase_histories_db.append(new_purchase_history)
        return new_purchase_history
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/purchase_histories/", response_model=List[PurchaseHistory])
async def read_purchase_histories(skip: int = 0, limit: int = 10):
    return purchase_histories_db[skip:skip + limit]


@router.get("/purchase_histories/{purchase_history_id}", response_model=PurchaseHistory)
async def read_purchase_history(purchase_history_id: int):
    purchase_history = next(
        (history for history in purchase_histories_db if history.id ==
         purchase_history_id), None
    )
    if purchase_history is None:
        raise HTTPException(
            status_code=404, detail="Purchase history not found")
    return purchase_history


@router.put("/purchase_histories/{purchase_history_id}", response_model=PurchaseHistory)
async def update_purchase_history(
    purchase_history_id: int, updated_purchase_history: PurchaseHistoryCreate
):
    purchase_history = next(
        (history for history in purchase_histories_db if history.id ==
         purchase_history_id), None
    )
    if purchase_history is None:
        raise HTTPException(
            status_code=404, detail="Purchase history not found")
    purchase_history_index = purchase_histories_db.index(purchase_history)
    purchase_histories_db[purchase_history_index] = PurchaseHistory(
        **updated_purchase_history.dict(), id=purchase_history_id
    )
    return purchase_histories_db[purchase_history_index]


@router.delete("/purchase_histories/{purchase_history_id}", response_model=dict)
async def delete_purchase_history(purchase_history_id: int):
    purchase_history = next(
        (history for history in purchase_histories_db if history.id ==
         purchase_history_id), None
    )
    if purchase_history is None:
        raise HTTPException(
            status_code=404, detail="Purchase history not found")
    purchase_histories_db.remove(purchase_history)
    return {"message": "Purchase history deleted"}

app.include_router(router, prefix="/purchase_history_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /purchase_history_api/purchase_histories/ - ایجاد تاریخچه خرید جدید
# GET    /purchase_history_api/purchase_histories/ - دریافت لیست تاریخچه‌های خرید
# GET    /purchase_history_api/purchase_histories/{id} - دریافت جزئیات یک تاریخچه خرید
# PUT    /purchase_history_api/purchase_histories/{id} - بروزرسانی اطلاعات یک تاریخچه خرید
# DELETE /purchase_history_api/purchase_histories/{id} - حذف یک تاریخچه خرید


# PurchaseHistoryProduct

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models برای داده‌های ورودی و خروجی


class PurchaseHistoryProductBase(BaseModel):
    purchase_history_id: int  # ارجاع به ID سابقه خرید
    product_name: str
    quantity: int
    unit_price: float
    total_price: float


class PurchaseHistoryProductCreate(PurchaseHistoryProductBase):
    pass


class PurchaseHistoryProduct(PurchaseHistoryProductBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
purchase_history_products_db = []

# عملیات CRUD


@router.post("/purchase_history_products/", response_model=PurchaseHistoryProduct)
async def create_purchase_history_product(purchase_history_product: PurchaseHistoryProductCreate):
    try:
        print("Received purchase history product data:",
              purchase_history_product.dict())
        new_product = PurchaseHistoryProduct(
            **purchase_history_product.dict(), id=len(purchase_history_products_db) + 1
        )
        purchase_history_products_db.append(new_product)
        return new_product
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/purchase_history_products/", response_model=List[PurchaseHistoryProduct])
async def read_purchase_history_products(skip: int = 0, limit: int = 10):
    return purchase_history_products_db[skip:skip + limit]


@router.get("/purchase_history_products/{product_id}", response_model=PurchaseHistoryProduct)
async def read_purchase_history_product(product_id: int):
    product = next(
        (prod for prod in purchase_history_products_db if prod.id == product_id), None
    )
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/purchase_history_products/{product_id}", response_model=PurchaseHistoryProduct)
async def update_purchase_history_product(
    product_id: int, updated_product: PurchaseHistoryProductCreate
):
    product = next(
        (prod for prod in purchase_history_products_db if prod.id == product_id), None
    )
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product_index = purchase_history_products_db.index(product)
    purchase_history_products_db[product_index] = PurchaseHistoryProduct(
        **updated_product.dict(), id=product_id
    )
    return purchase_history_products_db[product_index]


@router.delete("/purchase_history_products/{product_id}", response_model=dict)
async def delete_purchase_history_product(product_id: int):
    product = next(
        (prod for prod in purchase_history_products_db if prod.id == product_id), None
    )
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    purchase_history_products_db.remove(product)
    return {"message": "Product deleted"}

app.include_router(router, prefix="/purchase_history_product_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /purchase_history_product_api/purchase_history_products/ - ایجاد محصول مرتبط با تاریخچه خرید
# GET    /purchase_history_product_api/purchase_history_products/ - دریافت لیست محصولات تاریخچه خرید
# GET    /purchase_history_product_api/purchase_history_products/{id} - دریافت جزئیات یک محصول تاریخچه خرید
# PUT    /purchase_history_product_api/purchase_history_products/{id} - بروزرسانی اطلاعات محصول تاریخچه خرید
# DELETE /purchase_history_product_api/purchase_history_products/{id} - حذف محصول تاریخچه خرید

# BuyerAuthentication

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models برای داده‌های ورودی و خروجی


class BuyerAuthenticationBase(BaseModel):
    contact_number: bool = False  # شماره تماس
    national_id: bool = False  # کد ملی
    id_card_image: Optional[str] = None  # مسیر آپلود تصویر کارت ملی
    birth_certificate_image: Optional[str] = None  # مسیر آپلود تصویر شناسنامه
    # مسیر آپلود قرارداد ضمانت یا چک
    guarantee_or_check_contract: Optional[str] = None


class BuyerAuthenticationCreate(BuyerAuthenticationBase):
    pass


class BuyerAuthentication(BuyerAuthenticationBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
buyer_authentications_db = []

# عملیات CRUD


@router.post("/buyer_authentications/", response_model=BuyerAuthentication)
async def create_buyer_authentication(buyer_authentication: BuyerAuthenticationCreate):
    try:
        print("Received buyer authentication data:",
              buyer_authentication.dict())
        new_authentication = BuyerAuthentication(
            **buyer_authentication.dict(), id=len(buyer_authentications_db) + 1
        )
        buyer_authentications_db.append(new_authentication)
        return new_authentication
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/buyer_authentications/", response_model=List[BuyerAuthentication])
async def read_buyer_authentications(skip: int = 0, limit: int = 10):
    return buyer_authentications_db[skip:skip + limit]


@router.get("/buyer_authentications/{authentication_id}", response_model=BuyerAuthentication)
async def read_buyer_authentication(authentication_id: int):
    authentication = next(
        (auth for auth in buyer_authentications_db if auth.id == authentication_id), None
    )
    if authentication is None:
        raise HTTPException(
            status_code=404, detail="Buyer authentication not found")
    return authentication


@router.put("/buyer_authentications/{authentication_id}", response_model=BuyerAuthentication)
async def update_buyer_authentication(
    authentication_id: int, updated_authentication: BuyerAuthenticationCreate
):
    authentication = next(
        (auth for auth in buyer_authentications_db if auth.id == authentication_id), None
    )
    if authentication is None:
        raise HTTPException(
            status_code=404, detail="Buyer authentication not found")
    authentication_index = buyer_authentications_db.index(authentication)
    buyer_authentications_db[authentication_index] = BuyerAuthentication(
        **updated_authentication.dict(), id=authentication_id
    )
    return buyer_authentications_db[authentication_index]


@router.delete("/buyer_authentications/{authentication_id}", response_model=dict)
async def delete_buyer_authentication(authentication_id: int):
    authentication = next(
        (auth for auth in buyer_authentications_db if auth.id == authentication_id), None
    )
    if authentication is None:
        raise HTTPException(
            status_code=404, detail="Buyer authentication not found")
    buyer_authentications_db.remove(authentication)
    return {"message": "Buyer authentication deleted"}

app.include_router(router, prefix="/buyer_authentication_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /buyer_authentication_api/buyer_authentications/ - ایجاد اطلاعات احراز هویت
# GET    /buyer_authentication_api/buyer_authentications/ - دریافت لیست اطلاعات احراز هویت
# GET    /buyer_authentication_api/buyer_authentications/{id} - دریافت جزئیات یک احراز هویت
# PUT    /buyer_authentication_api/buyer_authentications/{id} - بروزرسانی اطلاعات احراز هویت
# DELETE /buyer_authentication_api/buyer_authentications/{id} - حذف اطلاعات احراز هویت


#

#

#

#

#

#

#

#

#

#

#

# app Product


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class ProductBase(BaseModel):
    image: Optional[str] = None  # مسیر آپلود تصویر
    name: str
    stock: int
    unit: str
    category: str
    brand: str
    purchase_price: float
    cover_price: float
    sale_price: float
    manufacture_date: str  # تاریخ ساخت به صورت رشته
    expiration_date: str  # تاریخ انقضا به صورت رشته
    sale_status: str
    marketer_profit: float
    turnover: int
    operations: str
    description: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
products_db = []

# عملیات CRUD


@router.post("/products/", response_model=Product)
async def create_product(product: ProductCreate):
    try:
        print("Received product data:", product.dict())
        new_product = Product(**product.dict(), id=len(products_db) + 1)
        products_db.append(new_product)
        return new_product
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/products/", response_model=List[Product])
async def read_products(skip: int = 0, limit: int = 10):
    return products_db[skip:skip + limit]


@router.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: int):
    product = next((p for p in products_db if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: ProductCreate):
    product = next((p for p in products_db if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product_index = products_db.index(product)
    products_db[product_index] = Product(
        **updated_product.dict(), id=product_id)
    return products_db[product_index]


@router.delete("/products/{product_id}", response_model=dict)
async def delete_product(product_id: int):
    product = next((p for p in products_db if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db.remove(product)
    return {"message": "Product deleted"}

app.include_router(router, prefix="/product_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /product_api/products/         - ایجاد محصول جدید
# GET    /product_api/products/         - دریافت لیست محصولات
# GET    /product_api/products/{id}     - دریافت جزئیات یک محصول خاص
# PUT    /product_api/products/{id}     - بروزرسانی اطلاعات یک محصول
# DELETE /product_api/products/{id}     - حذف یک محصول


#

#

#

#

#

#

#

#

#

#

#


# app  payment
# mainPayment
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class PaymentBase(BaseModel):
    first_name: str
    last_name: str
    store_name: str
    contact_number: str
    national_id: str
    province: str
    city: str
    location: str
    debt: float = 0.0
    financial_limit: float = 0.0
    history: Optional[str] = None
    notifications: Optional[str] = None
    operations: str


class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
payments_db = []

# عملیات CRUD


@router.post("/payments/", response_model=Payment)
async def create_payment(payment: PaymentCreate):
    try:
        print("Received payment data:", payment.dict())
        new_payment = Payment(**payment.dict(), id=len(payments_db) + 1)
        payments_db.append(new_payment)
        return new_payment
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/payments/", response_model=List[Payment])
async def read_payments(skip: int = 0, limit: int = 10):
    return payments_db[skip:skip + limit]


@router.get("/payments/{payment_id}", response_model=Payment)
async def read_payment(payment_id: int):
    payment = next((p for p in payments_db if p.id == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment


@router.put("/payments/{payment_id}", response_model=Payment)
async def update_payment(payment_id: int, updated_payment: PaymentCreate):
    payment = next((p for p in payments_db if p.id == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    payment_index = payments_db.index(payment)
    payments_db[payment_index] = Payment(
        **updated_payment.dict(), id=payment_id)
    return payments_db[payment_index]


@router.delete("/payments/{payment_id}", response_model=dict)
async def delete_payment(payment_id: int):
    payment = next((p for p in payments_db if p.id == payment_id), None)
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    payments_db.remove(payment)
    return {"message": "Payment deleted"}

app.include_router(router, prefix="/payment_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# MarketerPayment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models برای MarketerPayment


class MarketerPaymentBase(BaseModel):
    first_name: str
    last_name: str
    role: str
    contact_number: str
    national_id: str
    province: str
    city: str
    status: str
    wallet_balance: float = 0.0
    notifications: Optional[str] = None
    actions: Optional[str] = None


class MarketerPaymentCreate(MarketerPaymentBase):
    pass


class MarketerPayment(MarketerPaymentBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت برای MarketerPayment
marketer_payments_db = []

# عملیات CRUD برای MarketerPayment


@router.post("/marketer_payments/", response_model=MarketerPayment)
async def create_marketer_payment(marketer_payment: MarketerPaymentCreate):
    try:
        print("Received marketer payment data:", marketer_payment.dict())
        new_payment = MarketerPayment(
            **marketer_payment.dict(), id=len(marketer_payments_db) + 1)
        marketer_payments_db.append(new_payment)
        return new_payment
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/marketer_payments/", response_model=List[MarketerPayment])
async def read_marketer_payments(skip: int = 0, limit: int = 10):
    return marketer_payments_db[skip:skip + limit]


@router.get("/marketer_payments/{payment_id}", response_model=MarketerPayment)
async def read_marketer_payment(payment_id: int):
    marketer_payment = next(
        (payment for payment in marketer_payments_db if payment.id == payment_id), None)
    if marketer_payment is None:
        raise HTTPException(
            status_code=404, detail="Marketer payment not found")
    return marketer_payment


@router.put("/marketer_payments/{payment_id}", response_model=MarketerPayment)
async def update_marketer_payment(payment_id: int, updated_payment: MarketerPaymentCreate):
    marketer_payment = next(
        (payment for payment in marketer_payments_db if payment.id == payment_id), None)
    if marketer_payment is None:
        raise HTTPException(
            status_code=404, detail="Marketer payment not found")
    payment_index = marketer_payments_db.index(marketer_payment)
    marketer_payments_db[payment_index] = MarketerPayment(
        **updated_payment.dict(), id=payment_id)
    return marketer_payments_db[payment_index]


@router.delete("/marketer_payments/{payment_id}", response_model=dict)
async def delete_marketer_payment(payment_id: int):
    marketer_payment = next(
        (payment for payment in marketer_payments_db if payment.id == payment_id), None)
    if marketer_payment is None:
        raise HTTPException(
            status_code=404, detail="Marketer payment not found")
    marketer_payments_db.remove(marketer_payment)
    return {"message": "Marketer payment deleted"}


app.include_router(router, prefix="/marketer_payment_api")
app.include_router(router, prefix="/need_for_action_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /marketer_payment_api/marketer_payments/   - ایجاد اطلاعات مالی بازاریاب
# GET    /marketer_payment_api/marketer_payments/   - دریافت لیست اطلاعات مالی
# GET    /marketer_payment_api/marketer_payments/{id} - دریافت جزئیات یک پرداخت
# PUT    /marketer_payment_api/marketer_payments/{id} - بروزرسانی اطلاعات پرداخت
# DELETE /marketer_payment_api/marketer_payments/{id} - حذف اطلاعات پرداخت

# POST   /need_for_action_api/need_for_actions/     - ایجاد نیاز به اقدام
# GET    /need_for_action_api/need_for_actions/     - دریافت لیست نیازهای اقدام
# GET    /need_for_action_api/need_for_actions/{id} - دریافت جزئیات یک اقدام خاص
# PUT    /need_for_action_api/need_for_actions/{id} - بروزرسانی اطلاعات اقدام
# DELETE /need_for_action_api/need_for_actions/{id} - حذف اقدام


# HistoryMarketerPayment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class HistoryMarketerPaymentBase(BaseModel):
    history: str
    is_selected: bool = False
    total_paid_profit: float
    document: Optional[str] = None  # مسیر آپلود سند
    more_details: Optional[str] = None
    payment_date: str  # تاریخ پرداخت به صورت رشته


class HistoryMarketerPaymentCreate(HistoryMarketerPaymentBase):
    pass


class HistoryMarketerPayment(HistoryMarketerPaymentBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
history_marketer_payments_db = []

# عملیات CRUD


@router.post("/history_marketer_payments/", response_model=HistoryMarketerPayment)
async def create_history_marketer_payment(history_marketer_payment: HistoryMarketerPaymentCreate):
    try:
        print("Received history marketer payment data:",
              history_marketer_payment.dict())
        new_payment = HistoryMarketerPayment(
            **history_marketer_payment.dict(), id=len(history_marketer_payments_db) + 1
        )
        history_marketer_payments_db.append(new_payment)
        return new_payment
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/history_marketer_payments/", response_model=List[HistoryMarketerPayment])
async def read_history_marketer_payments(skip: int = 0, limit: int = 10):
    return history_marketer_payments_db[skip:skip + limit]


@router.get("/history_marketer_payments/{payment_id}", response_model=HistoryMarketerPayment)
async def read_history_marketer_payment(payment_id: int):
    payment = next(
        (pay for pay in history_marketer_payments_db if pay.id == payment_id), None
    )
    if payment is None:
        raise HTTPException(
            status_code=404, detail="History marketer payment not found")
    return payment


@router.put("/history_marketer_payments/{payment_id}", response_model=HistoryMarketerPayment)
async def update_history_marketer_payment(
    payment_id: int, updated_payment: HistoryMarketerPaymentCreate
):
    payment = next(
        (pay for pay in history_marketer_payments_db if pay.id == payment_id), None
    )
    if payment is None:
        raise HTTPException(
            status_code=404, detail="History marketer payment not found")
    payment_index = history_marketer_payments_db.index(payment)
    history_marketer_payments_db[payment_index] = HistoryMarketerPayment(
        **updated_payment.dict(), id=payment_id
    )
    return history_marketer_payments_db[payment_index]


@router.delete("/history_marketer_payments/{payment_id}", response_model=dict)
async def delete_history_marketer_payment(payment_id: int):
    payment = next(
        (pay for pay in history_marketer_payments_db if pay.id == payment_id), None
    )
    if payment is None:
        raise HTTPException(
            status_code=404, detail="History marketer payment not found")
    history_marketer_payments_db.remove(payment)
    return {"message": "History marketer payment deleted"}

app.include_router(router, prefix="/history_marketer_payment_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /history_marketer_payment_api/history_marketer_payments/    - ایجاد سابقه بازاریاب
# GET    /history_marketer_payment_api/history_marketer_payments/    - دریافت لیست سوابق بازاریاب
# GET    /history_marketer_payment_api/history_marketer_payments/{id} - دریافت جزئیات یک سابقه
# PUT    /history_marketer_payment_api/history_marketer_payments/{id} - بروزرسانی اطلاعات یک سابقه
# DELETE /history_marketer_payment_api/history_marketer_payments/{id} - حذف یک سابقه


# ProductPayment


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class ProductPaymentBase(BaseModel):
    image: Optional[str] = None  # مسیر آپلود تصویر
    product_name: str
    stock: int
    unit: str
    purchase_price: float
    sale_price: float
    cover_price: float
    operation: Optional[str] = None
    profit_percentage: float
    inventory_turnover: float
    sales_history: Optional[str] = None
    actions: Optional[str] = None


class ProductPaymentCreate(ProductPaymentBase):
    pass


class ProductPayment(ProductPaymentBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
product_payments_db = []

# عملیات CRUD


@router.post("/product_payments/", response_model=ProductPayment)
async def create_product_payment(product_payment: ProductPaymentCreate):
    try:
        print("Received product payment data:", product_payment.dict())
        new_payment = ProductPayment(
            **product_payment.dict(), id=len(product_payments_db) + 1)
        product_payments_db.append(new_payment)
        return new_payment
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/product_payments/", response_model=List[ProductPayment])
async def read_product_payments(skip: int = 0, limit: int = 10):
    return product_payments_db[skip:skip + limit]


@router.get("/product_payments/{payment_id}", response_model=ProductPayment)
async def read_product_payment(payment_id: int):
    product_payment = next(
        (pay for pay in product_payments_db if pay.id == payment_id), None
    )
    if product_payment is None:
        raise HTTPException(
            status_code=404, detail="Product payment not found")
    return product_payment


@router.put("/product_payments/{payment_id}", response_model=ProductPayment)
async def update_product_payment(
    payment_id: int, updated_payment: ProductPaymentCreate
):
    product_payment = next(
        (pay for pay in product_payments_db if pay.id == payment_id), None
    )
    if product_payment is None:
        raise HTTPException(
            status_code=404, detail="Product payment not found")
    payment_index = product_payments_db.index(product_payment)
    product_payments_db[payment_index] = ProductPayment(
        **updated_payment.dict(), id=payment_id
    )
    return product_payments_db[payment_index]


@router.delete("/product_payments/{payment_id}", response_model=dict)
async def delete_product_payment(payment_id: int):
    product_payment = next(
        (pay for pay in product_payments_db if pay.id == payment_id), None
    )
    if product_payment is None:
        raise HTTPException(
            status_code=404, detail="Product payment not found")
    product_payments_db.remove(product_payment)
    return {"message": "Product payment deleted"}

app.include_router(router, prefix="/product_payment_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST / product_payment_api/product_payments / - ایجاد سابقه محصول
# GET / product_payment_api/product_payments / - دریافت لیست سوابق محصولات
# GET / product_payment_api/product_payments/{id} - دریافت جزئیات یک سابقه محصول
# PUT / product_payment_api/product_payments/{id} - بروزرسانی اطلاعات یک سابقه محصول
# DELETE / product_payment_api/product_payments/{id} - حذف یک سابقه محصول


# BuyerPayment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class BuyerPaymentBase(BaseModel):
    full_name: str
    store_name: str
    phone_number: str
    national_code: str
    province: str
    city: str
    location: str
    debt: float
    financial_limit: float
    history: Optional[str] = None
    messenger: Optional[str] = None


class BuyerPaymentCreate(BuyerPaymentBase):
    pass


class BuyerPayment(BuyerPaymentBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
buyer_payments_db = []

# عملیات CRUD


@router.post("/buyer_payments/", response_model=BuyerPayment)
async def create_buyer_payment(buyer_payment: BuyerPaymentCreate):
    try:
        print("Received buyer payment data:", buyer_payment.dict())
        new_payment = BuyerPayment(
            **buyer_payment.dict(), id=len(buyer_payments_db) + 1)
        buyer_payments_db.append(new_payment)
        return new_payment
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/buyer_payments/", response_model=List[BuyerPayment])
async def read_buyer_payments(skip: int = 0, limit: int = 10):
    return buyer_payments_db[skip:skip + limit]


@router.get("/buyer_payments/{payment_id}", response_model=BuyerPayment)
async def read_buyer_payment(payment_id: int):
    buyer_payment = next(
        (pay for pay in buyer_payments_db if pay.id == payment_id), None
    )
    if buyer_payment is None:
        raise HTTPException(status_code=404, detail="Buyer payment not found")
    return buyer_payment


@router.put("/buyer_payments/{payment_id}", response_model=BuyerPayment)
async def update_buyer_payment(payment_id: int, updated_payment: BuyerPaymentCreate):
    buyer_payment = next(
        (pay for pay in buyer_payments_db if pay.id == payment_id), None
    )
    if buyer_payment is None:
        raise HTTPException(status_code=404, detail="Buyer payment not found")
    payment_index = buyer_payments_db.index(buyer_payment)
    buyer_payments_db[payment_index] = BuyerPayment(
        **updated_payment.dict(), id=payment_id
    )
    return buyer_payments_db[payment_index]


@router.delete("/buyer_payments/{payment_id}", response_model=dict)
async def delete_buyer_payment(payment_id: int):
    buyer_payment = next(
        (pay for pay in buyer_payments_db if pay.id == payment_id), None
    )
    if buyer_payment is None:
        raise HTTPException(status_code=404, detail="Buyer payment not found")
    buyer_payments_db.remove(buyer_payment)
    return {"message": "Buyer payment deleted"}

app.include_router(router, prefix="/buyer_payment_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# POST   /buyer_payment_api/buyer_payments/     - ایجاد پرداخت خریدار
# GET    /buyer_payment_api/buyer_payments/     - دریافت لیست پرداخت‌های خریدار
# GET    /buyer_payment_api/buyer_payments/{id} - دریافت جزئیات پرداخت خریدار
# PUT    /buyer_payment_api/buyer_payments/{id} - بروزرسانی اطلاعات پرداخت خریدار
# DELETE /buyer_payment_api/buyer_payments/{id} - حذف پرداخت خریدار


# app Order
# order

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# Pydantic Models


class OrderBase(BaseModel):
    buyer: str
    order_date: str  # تاریخ سفارش به صورت رشته
    order_number: str
    delivery_date: Optional[str] = None
    delivery_location: str
    product_id: str
    product_name: str
    quantity: int
    price: float
    discount: float = 0.0
    total_price: float
    payment_method: str
    order_method: str
    description: Optional[str] = None
    total_amount: float
    total_discount: float = 0.0
    shipping_cost: float = 0.0
    grand_total: float
    order_code: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        from_attributes = True


# دیتابیس موقت
orders_db = []

# عملیات CRUD


@router.post("/orders/", response_model=Order)
async def create_order(order: OrderCreate):
    try:
        print("Received order data:", order.dict())
        new_order = Order(**order.dict(), id=len(orders_db) + 1)
        orders_db.append(new_order)
        return new_order
    except ValidationError as e:
        print("Validation error:", e.errors())
        return JSONResponse(status_code=422, content={"detail": e.errors()})


@router.get("/orders/", response_model=List[Order])
async def read_orders(skip: int = 0, limit: int = 10):
    return orders_db[skip:skip + limit]


@router.get("/orders/{order_id}", response_model=Order)
async def read_order(order_id: int):
    order = next((o for o in orders_db if o.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, updated_order: OrderCreate):
    order = next((o for o in orders_db if o.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    order_index = orders_db.index(order)
    orders_db[order_index] = Order(**updated_order.dict(), id=order_id)
    return orders_db[order_index]


@router.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    order = next((o for o in orders_db if o.id == order_id), None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    orders_db.remove(order)
    return {"message": "Order deleted"}

app.include_router(router, prefix="/order_api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# تنظیمات پایگاه داده
# DATABASE_URL = "postgresql+psycopg2://pirdadeh:pirdadeh@localhost:5432/HP"


# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # مدل دیتابیس با SQLAlchemy


# class Order(Base):
#     __tablename__ = "orders"

#     id = Column(Integer, primary_key=True, index=True)
#     buyer = Column(String, nullable=False)
#     order_date = Column(String, nullable=False)
#     order_number = Column(String, nullable=False)
#     delivery_date = Column(String, nullable=True)
#     delivery_location = Column(String, nullable=False)
#     product_id = Column(String, nullable=False)
#     product_name = Column(String, nullable=False)
#     quantity = Column(Integer, nullable=False)
#     price = Column(Float, nullable=False)
#     discount = Column(Float, default=0.0)
#     total_price = Column(Float, nullable=False)
#     payment_method = Column(String, nullable=False)
#     order_method = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     total_amount = Column(Float, nullable=False)
#     total_discount = Column(Float, default=0.0)
#     shipping_cost = Column(Float, default=0.0)
#     grand_total = Column(Float, nullable=False)
#     order_code = Column(String, nullable=True)


# # ایجاد جداول دیتابیس
# Base.metadata.create_all(bind=engine)

# # تنظیمات FastAPI
# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# router = APIRouter()

# # مدل‌های Pydantic


# class OrderBase(BaseModel):
#     buyer: str
#     order_date: str  # تاریخ سفارش به صورت رشته
#     order_number: str
#     delivery_date: Optional[str] = None
#     delivery_location: str
#     product_id: str
#     product_name: str
#     quantity: int
#     price: float
#     discount: float = 0.0
#     total_price: float
#     payment_method: str
#     order_method: str
#     description: Optional[str] = None
#     total_amount: float
#     total_discount: float = 0.0
#     shipping_cost: float = 0.0
#     grand_total: float
#     order_code: Optional[str] = None


# class OrderCreate(OrderBase):
#     pass


# class OrderResponse(OrderBase):
#     id: int

#     class Config:
#         orm_mode = True

# # وابستگی دیتابیس


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # عملیات CRUD


# @router.post("/orders/", response_model=OrderResponse)
# async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
#     db_order = Order(**order.dict())
#     db.add(db_order)
#     db.commit()
#     db.refresh(db_order)
#     return db_order


# @router.get("/orders/", response_model=List[OrderResponse])
# async def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     orders = db.query(Order).offset(skip).limit(limit).all()
#     return orders


# @router.get("/orders/{order_id}", response_model=OrderResponse)
# async def read_order(order_id: int, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order


# @router.put("/orders/{order_id}", response_model=OrderResponse)
# async def update_order(order_id: int, updated_order: OrderCreate, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     for key, value in updated_order.dict().items():
#         setattr(order, key, value)
#     db.commit()
#     db.refresh(order)
#     return order


# @router.delete("/orders/{order_id}", response_model=dict)
# async def delete_order(order_id: int, db: Session = Depends(get_db)):
#     order = db.query(Order).filter(Order.id == order_id).first()
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     db.delete(order)
#     db.commit()
#     return {"message": "Order deleted"}

# app.include_router(router, prefix="/order_api")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)

# POST   /order_api/orders/     - ایجاد سفارش جدید
# GET    /order_api/orders/     - دریافت لیست سفارش‌ها
# GET    /order_api/orders/{id} - دریافت جزئیات یک سفارش
# PUT    /order_api/orders/{id} - بروزرسانی اطلاعات یک سفارش
# DELETE /order_api/orders/{id} - حذف یک سفارش
