from pydantic import BaseModel
from typing import Optional

class ProductModel(BaseModel):
    name: str
    categoryId: int
    description: Optional[str]

class CategoryModel(BaseModel):
    name: str