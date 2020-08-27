import pymysql



conn=None
# connection with database
def connect():
	global conn
	conn= pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass = pymysql.cursors.DictCursor)

#return the two record from person table at a time
def get_people(s):
	if (not conn):
		connect();
	
	query="select * from person LIMIT %s,2"
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query,(s))
		x=cursor.fetchall()
		return x	

# get the countries by independence year
def get_countries(number):
	if (not conn):
		connect();
	
	query="select Name, Continent,IndepYear from country Where IndepYear = %s"
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query,(number))
		x=cursor.fetchall()
		return x
		
# get the information from country table		
def get_countriesbyname():
	if (not conn):
		connect();
		
	query= "select code,Name, Continent,Population ,HeadofState from country"
	
	with conn:
		cursor = conn.cursor()
		cursor.execute(query)
		x=cursor.fetchall()
		return x
# add a new person in person table		
def add_aperson(name,age):
	if (not conn):
		connect();
	
	query= "INSERT INTO Person (personname , age) VALUES (%s,%s)"
	
	with conn:
		try:
			cursor = conn.cursor()
			cursor.execute(query,(name,age))
			conn.commit()
		except pymysql.err.IntegrityError as e:
			print ("***Error***",name ,"already exists")
		except pymysql.err.InternalError as e:
			print(e)
		except Exception as e:
			print(e)