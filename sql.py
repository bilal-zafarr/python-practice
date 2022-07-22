import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "CA")

# mycursor.execute(sql, val)

# mydb.commit()


sql = "DELETE FROM customers WHERE id = 2"

mycursor.execute(sql)

mydb.commit()