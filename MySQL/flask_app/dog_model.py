from mysqlconnection import connectToMySQL
DATEBASE = 'dogs'

class Dog:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.color = data['color']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs"
        results = connectToMySQL(DATEBASE).query_db(query)
        # print(results)
        all_dogs = []
        for row_from_db in results:
            dog_instance = cls(row_from_db) #instantiates dog object from ron in db
            all_dogs.append(dog_instance) #adds instance to list of instances
        return all_dogs

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dogs (name, breed, color, age) VALUES (%(name)s, %(breed)s, %(color)s, %(age)s)"
        return connectToMySQL(DATEBASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s;"
        results = connectToMySQL(DATEBASE).query_db(query,data)
        if len(results) > 0:
            dog_instance = cls(results[0])
            return dog_instance
        return False

    @classmethod
    def update(cls, data):
        query = "UPDATE dogs SET name = %(name)s, breed = %(breed)s, color = %(color)s, age = %(age)s WHERE id = %(id)s"
        return connectToMySQL(DATEBASE).query_db(query, data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"
        return connectToMySQL(DATEBASE).query_db(query, data)