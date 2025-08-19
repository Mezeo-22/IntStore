from fastapi import APIRouter, Query
from typing import Optional
from prisma import Prisma

from controller.models import ProductModel
from controller.products_controller import ProductController
from model.connect_to_db import db

router = APIRouter(prefix="/products", tags=["Products"])
product_controller = ProductController()

@router.get("/{id}")
async def get_one_product(id: int):
    return await product_controller.get_one_product(id)

@router.get("/")
async def get_all_products(page: int = Query(1), 
                           limit: int = Query(10),
                           categoryId: Optional[int] = Query(None)):
    return await product_controller.get_all_products(page, limit, categoryId)

@router.post("/")
async def post_product(product: ProductModel):
    return await product_controller.post_product(product)

@router.put("/{id}")
async def put_product(id: int, product: ProductModel):
    return await product_controller.put_product(id, product)

@router.delete("/{id}")
async def delete_product(id: int):
    return await product_controller.delete_product(id)