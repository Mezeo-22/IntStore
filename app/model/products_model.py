
class ProductQueries:

    def __init__(self, db):
        self.db = db

    def db_get_one_product(self, id):
        return self.db.product.find_unique(
            where={
                'id': id
            }
        )

    def db_get_all_products(self, skip, limit, where_conditions):
        return self.db.product.find_many(
            skip=skip, take=limit, where=where_conditions, order={"id": "asc"}, include={'category': True}
        )

    def db_post_product(self, product):
        return self.db.product.create(
            data={
                'name': product.name,
                'categoryId': product.categoryId,
                'description': product.description
            }
        )

    def db_put_product(self, id, product):
        return self.db.product.update(
            data={
                "name": product.name,
                "categoryId": product.categoryId,
                "description": product.description
            }, where={'id': id}
        )
    
    def db_delete_product(self, id):
        return self.db.product.delete(
        where={'id': id}
    )