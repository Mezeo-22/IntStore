from typing import Optional
from model.products_model import ProductQueries
from .models import ProductModel
from prisma import Prisma
from model.connect_to_db import db

class ProductController:

    def __init__(self):
        self.product_query = ProductQueries(db)

    async def get_one_product(self, id: int):

        if not isinstance(id, (int)) and id <= 0:
            return {"code": 400, "message": ["Некорректный id товара!"]}
        
        return await self.product_query.db_get_one_product(id)

    async def get_all_products(self, page: int, limit: int, categoryId: Optional[int]):

        errors = []
        if not isinstance(categoryId, (int)) and categoryId is not None:
            errors.append("Некорректный id категории!")
        if (not isinstance(page, (int)) and page < 1) or (not isinstance(limit, (int)) and limit < 1):
            errors.append("Некорректные параметры страницы!")

        if len(errors) > 0:
            return {"code": 400, "message": errors}
        
        skip = (page - 1) * limit
        where_conditions = {}
        if categoryId is not None:
            where_conditions['categoryId'] = categoryId

        products = await self.product_query.db_get_all_products(skip, limit, where_conditions)
        return {
            "code": 200,
            "page": page,
            "limit": limit,
            "products": products
        }
    
    async def post_product(self, product: ProductModel):
        
        errors = self.get_errors_in_product(product)
        if errors.count > 0:
            return {"code": 400, "message": errors}

        new_product = await self.product_query.db_post_product(product)
        return {"code": 200, "product": new_product}

    async def put_product(self, id: int, product: ProductModel):

        errors = self.get_errors_in_product(product)
        if errors.count > 0:
            return {"code": 400, "message": errors}
        
        upd_product = await self.product_query.db_put_product(id, product)
        return {"code": 200, "product": upd_product}

    async def delete_product(self, id: int):

        if not isinstance(id, (int)) and id <= 0:
            return {"code": 400, "message": ["Некорректный id товара!"]}
        
        del_product = await self.product_query.db_delete_product(id)
        return {"code": 200, "product": del_product}
    
    def get_errors_in_product(product: ProductModel):
        errors = []
        if product.name is None or product.name == "":
            errors.append("Имя товара не может быть пустым!")
        if isinstance(product.categoryId, (int)) or product.categoryId <= 0:
            errors.append("Некорректная категория товара!")
        
        return errors