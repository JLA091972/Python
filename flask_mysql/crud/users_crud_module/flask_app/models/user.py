# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

#define Database name
DATABASE = 'users_cr'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    ## CRUD
    # Create user accounts
    @classmethod
    def create_new_user(cls, data):
        query = "INSERT INTO users_cr.users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        connectToMySQL(DATABASE).query_db(query, data)

    # Read DB
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for friend in results:
            users.append( cls(friend) )
        return users

    ## Read One user
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users where id = %(id)s;"
        userinfo=connectToMySQL(DATABASE).query_db(query, data)  ## userinfo is a list of dictionary
        pprint(userinfo[0])
        user = User(userinfo[0])  ## need to get the dictionary out of the list to pass it to user
        print(user)
        return user

    # Update
    # this will update a user
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name= %(first_name)s, last_name = %(last_name)s, email = %(email)s where id = %(id)s"
        pprint(query)
        return connectToMySQL(DATABASE).query_db(query, data)


    # DELETE
    # this will delete a user
    @classmethod
    def delete_user(cls, data):
        pprint(data)
        query = "DELETE FROM users WHERE id = %(id)s;"
        pprint(query)
        return connectToMySQL(DATABASE).query_db(query, data)