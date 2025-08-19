
class CategoryQueries:

    def __init__(self, db):
        self.db = db

    def db_get_one_category(self, id):
        return self.db.category.find_unique(
            where={
                'id': id
            }
        )

    def db_get_all_category(self, skip, limit):
        return self.db.category.find_many(
            skip=skip, take=limit, order={"id": "asc"}
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
    
    def db_delete_category(self, id):
        return self.db.category.delete(
        where={'id': id}
    )