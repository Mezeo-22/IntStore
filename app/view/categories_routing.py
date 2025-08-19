from fastapi import APIRouter, Query

from controller.models import CategoryModel
from controller.categories_controller import CategoryController
from model.connect_to_db import db

router = APIRouter(prefix="/categories", tags=["Categories"])
category_controller = CategoryController()

@router.get("/{id}")
async def get_one_category(id: int):
    return await category_controller.get_one_category(id)

@router.get("/")
async def get_all_categories(page: int = Query(1), 
                           limit: int = Query(10)):
    return await category_controller.get_all_categories(page, limit)

@router.post("/")
async def post_category(category: CategoryModel):
    return await category_controller.post_category(category)

@router.put("/{id}")
async def put_category(id: int, category: CategoryModel):
    return await category_controller.put_category(id, category)

@router.delete("/{id}")
async def delete_category(id: int):
    return await category_controller.delete_category(id)