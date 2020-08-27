import project2DB # pymysql code for fetching data from MySQL
import projmongo #pymongo code for fetching data from mongoDB
#import re
# Initialise varable
data = None

def main():
	# display the menu
	display_menu()
	
	while True:
		
		choice = input("Enter choice: ") # input the user's choice
		
		if (choice == "1"): # View the people
			view_people()
			display_menu()
		elif (choice == "2"): #print countries according to Independence Year
			print_countries() 
			display_menu()
		elif (choice == "3"): # Add a  new person 
			add_person() 
			display_menu()
		elif (choice == "4"):# show countries by names
			view_byname(4) 
			display_menu()
		elif (choice == "5"): # show countries by population
			view_byname(5) 
			display_menu()
		elif (choice == "6"): # Find a student according to address
			find_student()
			display_menu()
		elif (choice == "7"): #Add a new course 
			add_course()
			display_menu()
		elif (choice == "x"):
			break;
		else:
			display_menu()

# function to view the people			
def view_people():
	print("Choice: 1")
	print()
	quit = " " # initialize a variable to use in loop
	start =0 
	# while loop until user input q
	while (quit != "q"):
		persons = project2DB.get_people(start)# start variable is to use in limit statement as we want only two rows at a time
	
		for person in persons:
			print(person["personID"],"|",person["personname"],"|",person["age"])
		start+=2
		# ask user to input q to quit otherwise again print next two rows of data
		quit= input("___Quit(q)__")

# method to print countries by Independence Year			
def print_countries():
	print("Choice: 2")
	print()
	print("Countries By Idependent Year")
	print("-" * 28)
	# ask the user to input the Year
	indep_Year= input("Enter Year:")
	countries = project2DB.get_countries(indep_Year)
	
	for country in countries:
		print(country["Name"],"|",country["Continent"],"|",country["IndepYear"])

# method to Add a person in the database
def add_person():
	print("Choice: 3")
	print()
	print("Add New Person")
	print("-" * 17)
	name = input("Name:")
	age = int(input("Age:"))
	
	project2DB.add_aperson(name,age)

# method for both choice 4 and 5 countries by name and population		
def view_byname(id):
	#global x
	
	global data
	if (not data):
		data = project2DB.get_countriesbyname()
		
	if (id==4):
		print("Choice: 4")
		print()
		print("Countries By Name")
		print("-" * 17)
		name = input("Enter Country Name:")
		name=name.lower()
		
		for country in data:
			cname=country["Name"].lower()
			if(cname.find(name)!=-1):# print the countries that have given substring in their name
				print(country["Name"],"|",country["Continent"],"|",country["Population"],"|",country["HeadofState"])
	elif (id==5):
		print("Choice: 5")
		print("")
		print("Countries By Pop")
		print("-" * 16)
		while True:
			sign = input("Enter < > or =:")
			if(sign=="=")or (sign==">")or(sign =="<"):
				break;
		s = sign
		pop= int(input("Enter Population:"))# ask the user to input population
		# print the rows according to the choice of sign and population
		if (s ==">"):
			for country in data:
				if(int(country["Population"])>pop):
					print(country["code"],"|",country["Name"],"|",country["Continent"],"|",country["Population"])
		elif (s =="<"):
			for country in data:
				if(int(country["Population"])< pop):
					print(country["code"],"|",country["Name"],"|",country["Continent"],"|",country["Population"])
		elif (s =="="):
			for country in data:
				if(int(country["Population"])== pop):
					print(country["code"],"|",country["Name"],"|",country["Continent"],"|",country["Population"])

# function to find the student according to the address input by user
def find_student():
	print("Choice: 6")
	print()
	print("Find a Student by Address")
	print("-" * 27)
	
	address= input("Enter Address:")
	projmongo.find_student(address)

#function to add new course
def add_course():
	print("Choice: 7")
	print()

	print("Add New Course")
	print("-" * 27)
	
	id = input("_id:")
	cname = input("Name:")
	level = int(input("Level:"))
	
	projmongo.add_course(id,cname,level)
	

# display menu
def display_menu():

    print("World DB")
    print("-" * 8)
    print("MENU")
    print("=" * 4)
    print("1 - View People")
    print("2 - View Countries by Independence Year")
    print("3 - Add New Person")
    print("4 - View Countries by name")
    print("5 - View Countries by population")
    print("6 - Find Student by Address")
    print("7 - Add New Course")
    print("x - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()