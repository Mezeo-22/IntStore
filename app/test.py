from fastapi import FastAPI, Query
from fastapi.concurrency import asynccontextmanager
from typing import Optional
from prisma import Prisma
from pydantic import BaseModel
import uvicorn

class ProductModel(BaseModel):
    name: str
    categoryId: int
    description: Optional[str]

class CategoryModel(BaseModel):
    name: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)
db = Prisma()

# CRUD Products
@app.get("/products/{id}")
async def get_one_product(id: int):
    product = await db.product.find_unique(
        where={
            'id': id
        }
    )
    return product

@app.get("/products")
async def get_all_products(page: int = Query(1, ge=1), 
                           limit: int = Query(10, ge=1, le=20),
                           categoryId: Optional[int] = Query(None)):
    if not isinstance(categoryId, (int)) and categoryId is not None:
        return {"error": "categoryId is not int"}
    skip = (page - 1) * limit
    where_conditions = {}
    if categoryId is not None:
        where_conditions['categoryId'] = categoryId
    products = await db.product.find_many(
        skip=skip, take=limit, where=where_conditions, order={"id": "asc"}
    )
    return {"page": page, "limit": limit, "products": products}

@app.post("/products")
async def post_product(product: ProductModel):
    new_product = await db.product.create(
        data={
            'name': product.name,
            'categoryId': product.categoryId,
            'description': product.description
        }
    )
    return {"message": "done", "product": new_product}

@app.put("/products/{id}")
async def put_product(id: int, product: ProductModel):
    upd_product = await db.product.update(
        data={
            "name": product.name,
            "categoryId": product.categoryId,
            "description": product.description
        }, where={'id': id}
    )
    return upd_product

@app.delete("/products/{id}")
async def delete_product(id: int):
    del_product = await db.product.delete(
        where={'id': id}
    )
    return del_product

# CRUD Categories
@app.post("/categories")
async def post_category(category: CategoryModel):
    category = await db.category.create(
        data={"name": category.name}
    )
    return category

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)