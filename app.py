from flask import Flask, jsonify, request, render_template     

app = Flask(__name__) 
stores = [
    {
        'name': 'My Wonderful Store',
        'items':[
            {
                'name': 'My Item',
                'price': 15.99,

            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('template\index.html')
 

#POST - used to receive data
#GET - used to send data back only

#1. Post /store data: {name:} : Create a new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)   
    return jsonify(new_store)

#2. GET /store/<string:name> : return a store with a given name
@app.route('/store/<string:name>') #'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    #Iterate over stores
    #if the store name matches, return it
    #if non match, return an error message

    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
        

#3. GET /store : return a list of all the stores
@app.route('/store') #'http://127.0.0.1:5000/store/some_name'
def get_stores():
    return jsonify({'stores': stores}) #convert store variable in to Json

#4. POST /store/<string:name>/item {name:, price:} :Create an item inside a specific store, with a given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
            'name': request_data['name'],
            'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})



#5. GET /store/<string:name>/item : Return all the items in a specific store  
@app.route('/store/<string:name>/item') 
def get_item_in_store(name):
    for store in stores:
        if store['name'] ==  name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'store not found'})



app.run(port=5000)

#test2