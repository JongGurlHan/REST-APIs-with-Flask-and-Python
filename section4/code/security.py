from user import User 

users = [
    User(1, 'bob', 'adsf')
]

# username_mapping = { 'bob' : {
#         'id': 1,
#         'username' : 'bob',
#         'password' : 'asdf'
#     }
# }

# userid_mapping = { 1 :{
#         'id': 1,
#         'username' : 'bob',
#         'password' : 'asdf'
#     }
# }

username_mapping = {u.username : u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None) #.get: is another way of accessing a dictionary, 
                                                #it gives us the value of the key
    if user and user.password == password :
        return user                                           

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

# the identity function takes in a payload
# and the payload is the contents of the JWT Token

# and then we're going to extract the user ID from that payload
# and once we have the user ID, we can retrieve the specific user that matches this payload
# by just doing return userID_mapping.get(userID) or none as a default.