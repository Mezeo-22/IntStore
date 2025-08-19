
#PRODUCT 
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
            skip=skip, take=limit, where=where_conditions, order={"id": "asc"}
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


#CATEGORY
class CategoryQueries:

    def __init__(self, db):
        self.db = db

    def db_get_one_category(self, id):
        return self.db.category.find_unique(
            where={
                'id': id
            }
        )

    def db_get_all_category(self, skip, limit, where_conditions):
        return self.db.category.find_many(
            skip=skip, take=limit, where=where_conditions, order={"id": "asc"}
        )

    def db_post_category(self, category):
        return self.db.category.create(
            data={"name": category.name}
        )
    
    def db_put_category(self, id, category):
        return self.db.category.update(
            data={
                "name": category.name
            }, where={'id': id}
        )
    
    def db_delete_product(self, id):
        return self.db.category.delete(
        where={'id': id}
    )