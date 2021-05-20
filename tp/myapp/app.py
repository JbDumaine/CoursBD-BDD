# Module Imports
import mysql.connector as database



connection = database.connect(
    user='root',
    password='root',
    host='localhost',
    database="classicmodels")

cursor = connection.cursor()


def get_all_customer():
    try:
      statement = "SELECT contactLastName, contactFirstName FROM customers LIMIT 5"
      cursor.execute(statement)
      for (contactLastName, contactFirstName) in cursor:
        print(f"Successfully retrieved {contactLastName}, {contactFirstName}")
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")

def get_offices_list():
    try:
      statement = "SELECT officeCode, city, phone, addressLine1, addressLine2, state,country, postalCode, territory FROM offices ORDER BY country, state, city"
      cursor.execute(statement)
      for (officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) in cursor:
        print(f"{officeCode} {city} {state} {country}")
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")

def count_employees():
    try:
      statement = "SELECT COUNT(*) FROM employees"
      cursor.execute(statement)
      for count in cursor:
        print(f"Il y a {count[0]} employes!")
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")

def totalpayement():
    try:
      statement = "SELECT SUM(amount) FROM payments"
      cursor.execute(statement)
      for count in cursor:
        print(f"{count[0]} boulas!")
    except database.Error as e:
      print(f"Error retrieving entry from database: {e}")

#get_all_customer()
get_offices_list()
count_employees()
totalpayement()

