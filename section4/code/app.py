from flask import Flask
from flask_restful import Resource, Api #Resource is just a thing that our API can return and create and things like that
from flask_jwt import JWT, jwt_required                            

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)
    #Api is just going to allow us to very easily add these Resources to it 

jwt = JWT(app, authenticate, identity)
#JWT creates a new endpoint that endpoint is /auth,/auth
# when we call /auth, we send it a username and password 
# and the JWT extension gets that username and password and sends it over to the authenticate function  
# We are then going to find the correct user object using that username
#and we're going to compare its password to the one that we receive through the auth endpoint
# if they match we're going to return the user and that becomes sort of the identity 

#so what happends next is the auth endpoint returns a JW token
# Now that JW token in itself doesn't do anything, but we can send it to the next request we make.  

#what JWT does is it calls the identity function. and then it uses the JWT token to get the user ID
#and with that it gets the correct user for that user ID that the JWT token represents.    
items =[]




#Api works with resources and every resouce has to be a class
#class Item inherits from from the class resource 
class Item(Resource):  
   # @app.route('/item/<string:name>')
    @jwt_required
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #we're going to go through each item, execute this function  
                                                                     #and see if the item's name x matches the name which is the parameter
                                                                     #And if it does, then we're going to return it

                                                                    #None: if the next function doesn't find an item,
                                                                    #       it will just return none
        # for item in items:
        #     if item['name'] ==name:
        #         return item
        
        return {'item' : item}, 200 if item else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}'is already exists".format(name)}, 400
        
        item = {'name': name, 'price': 12.00}
        items.append(item)
     
class ItemList(Resource):
    def get(self):
        return {'items': items}

 
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
#tell our API, This resouce that we've created, the student, now is gonna be accessible via our API,
# '/item/<string:name>': we're going to access students like so 
#This name variable is going to go straight in to the parameter'name'
app.run(port=5000, debug=True)
