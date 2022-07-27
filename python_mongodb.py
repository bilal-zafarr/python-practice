import pymongo

client = pymongo.MongoClient()

db = client["mydatabse"]

col = db["customers"]

mydict = {
    "name": "Bilal",
    "address": "Lahore"
}

mylist = [
    {
        "name": "Bilal",
        "address": "Lahore"
    },
    {
        "name": "Amir",
        "address": "Lahore"
    }
]

# res = col.insert_many(mylist)

#print(client.list_database_names())
#col.insert_many(mylist)

col.update_many({"name": "Bilal"}, {"$set": {"address": "FSD"}})

myresult = col.find().limit(50)

#print the result:
for x in myresult:
  print(x)


# for x in col.find({},{"_id":0, "name":1}):
#     print(x)

#col.drop()

client.close()