from .products_routing import router as product_router
from .categories_routing import router as category_router

routers = [
    product_router,
    category_router
]