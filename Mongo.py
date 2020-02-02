from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbspartaName
#
# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':35})
# db.users.insert_one({'name':'john','age':40})
# db.users.insert_one({'name':'pak','age':25})

all_users = list(db.users.find({}))

same_ages = list(db.users.find({'age':21}))

print(all_users[0])
print(all_users[0]['name'])

for user in all_users:
    print(user['name'])

user = db.users.find_one({'name':'bobby'})
print(user)

user = db.users.find_one({'name':'bobby'},{'_id':0})
print(user)

db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)


