from flask import Flask
from flask_restful import Resource, Api
                            #Resource is just a thing that our API can return and create and things like that
app = Flask(__name__)

api = Api(app)
    #Api is just going to allow us to very easily add these Resources to it 

items =[]




#Api works with resources and every resouce has to be a class
#class Item inherits from from the class resource 
class Item(Resource):  
   # @app.route('/item/<string:name>')
    def get(self, name):
       item = filter(lambda x: x['name'] == name, items) #we're going to go through each item, execute this function  
                                                         #and see if the item's name x matches the name which is the parameter
                                                         #And if it does, then we're going to return it
       
        # for item in items:
        #     if item['name'] ==name:
        #         return item
        return {'item' : None}, 404
    
    def post(self, name):
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
