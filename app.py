from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")
db=client['test']
#db.Demo.insert_many([{"Name":"Kamal","Age":20},{"Name":"Nishanth","Age":5}])
#db.Demo.insert_one({"Address":"Sarvam","City":"Chennai"})
for i in db.Demo.find({"Name":{"$regex":"\w"}},{"_id":0}):
	print(i)
print(db.Demo.count_documents({"Name":{"$regex":"\w"}})) 
print(db.Demo.count_documents({})) 
cursor = db.Demo.find({},{"_id":0}) 
for i in cursor:
    print(i)