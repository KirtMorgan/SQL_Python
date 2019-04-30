import pyodbc
# Our variables to create a connection
connection = 'Microsoft SQL Server'
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Making a connection
docker_northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

# Creating a cursor that can execute SQL functions on connected database
cursor = docker_northwind.cursor()

# Executing the SQL
query = cursor.execute('SELECT * FROM Customers')

# Getting results from above SQL execution
rows = query.fetchall()
# print(rows)
for data in rows:
    print('My name is',data.ContactName)