from model.categories_model import CategoryQueries
from .models import CategoryModel
from model.connect_to_db import db

class CategoryController:

    def __init__(self):
        self.category_queries = CategoryQueries(db)

    async def get_one_category(self, id: int):

        if not isinstance(id, (int)) and id <= 0:
            return {"code": 400, "message": ["Некорректный id категории!"]}
        
        return await self.category_queries.db_get_one_category(id)

    async def get_all_categories(self, page: int, limit: int):

        errors = []
        if (not isinstance(page, (int)) and page < 1) or (not isinstance(limit, (int)) and limit < 1):
            errors.append("Некорректные параметры страницы!")

        if len(errors) > 0:
            return {"code": 400, "message": errors}
        
        skip = (page - 1) * limit

        categories = await self.category_queries.db_get_all_category(skip, limit)
        return {
            "code": 200,
            "page": page,
            "limit": limit,
            "products": categories
        }
    
    async def post_category(self, category: CategoryModel):
        
        errors = self.get_errors_in_category(category)
        if errors.count > 0:
            return {"code": 400, "message": errors}

        new_category = await self.category_queries.db_post_category(category)
        return {"code": 200, "category": new_category}

    async def put_category(self, id: int, category: CategoryModel):

        errors = self.get_errors_in_category(category)
        if errors.count > 0:
            return {"code": 400, "message": errors}
        
        upd_category = await self.category_queries.db_put_category(id, category)
        return {"code": 200, "category": upd_category}

    async def delete_category(self, id: int):

        if not isinstance(id, (int)) and id <= 0:
            return {"code": 400, "message": ["Некорректный id категории!"]}
        
        del_category = await self.category_queries.db_delete_category(id)
        return {"code": 200, "category": del_category}
    
    def get_errors_in_category(category: CategoryModel):
        errors = []
        if category.name is None or category.name == "":
            errors.append("Имя категории не может быть пустым!")
        
        return errors