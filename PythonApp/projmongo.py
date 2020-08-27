import pymongo
from bson.int64 import Int64

myclient =None

def connect():
	global myclient
	myclient= pymongo.MongoClient()
	myclient.admin.command("ismaster")

# find a student 
def find_student(address):
	#if (not myclient):
		try:
			connect()
			mydb=myclient["proj20DB"]
			docs= mydb["docs"]
			#db.docs.aggregate([{$match:{details:{$exists:true}, "details.address":"Galway"}},{$project:{qualifications:{$ifNull:["$qualifications",""]}}}])
			#var regex = new RegExp(["^", address, "$"].join(""), "i")
			#query= { "$match":{"details":{"$exists":"true"},"details.address": regex}}
			#{"$text":{"$search": address,"$caseSensitive": "False"}}
			#query= { "$match":{"details.address": {"$text":{"$search": address,"$caseSensitive": "false"}},"details":{"$exists":"true"}}}
			
			query= { "$match":{"details":{"$exists":"true"},"details.address": address}}
			
			p= {"$project":{ "details.name":1,"details.address":1,"details.age":1,"qualifications":{"$ifNull":["$qualifications",""]}}}
			people = docs.aggregate([query,p])
			
			for p in people:
				print(p["_id"],"|",p["details"]["name"],"|",p["details"]["address"],"|",int(p["details"]["age"]),"|",p["qualifications"])
		except Exception as e:
			print("Error",e)

#add a course	
def add_course(id,cname,clevel):
	
	try:
		connect()
		mydb=myclient["proj20DB"]
		docs= mydb["docs"]
		x = "_id"
		name = "name"
		level="level"
		#print(clevel)
		
		newDocs={x:id,name:cname,level:int(clevel)}
		result= docs.insert_one(newDocs)
		
		print("COURSE is added id= "+result.inserted_id)
		

	except pymongo.errors.DuplicateKeyError as e:
		print("***ERROR*** _id DATA already exists")
	except Exception as e:
		print("Error",e)
		
	
