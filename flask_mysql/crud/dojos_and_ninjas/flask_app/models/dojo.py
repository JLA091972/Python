# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint
from flask_app.models.ninja import Ninja

# define Database name
DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # CRUD
    # Create dojo accounts
    @classmethod
    def create_new_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        connectToMySQL(DATABASE).query_db(query, data)

    # Read DB
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    # Read One dojo
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos where id = %(id)s;"
        dojoinfo = connectToMySQL(DATABASE).query_db(
            query, data)  # dojoinfo is a list of dictionary
        pprint(dojoinfo[0])
        # need to get the dictionary out of the list to pass it to dojo
        dojo = Dojo(dojoinfo[0])
        print(dojo)
        return dojo

    # Read list of Ninja in a Dojo
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id where dojos.id = %(id)s"
        ninjalist = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(ninjalist[0])
        pprint(dojo.name)
            
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        for eachninja in ninjalist:
            tempninja = {
                'id' : eachninja['ninjas.id'],
                'first_name' : eachninja['first_name'],
                'last_name' : eachninja['last_name'],
                'age' : eachninja['age'],
                'dojo_id' : eachninja['dojo_id'],
                'created_at' : eachninja['ninjas.created_at'],
                'updated_at' : eachninja['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(tempninja))
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        pprint(dojo)
        return dojo

    # Update
    # this will update a dojo
