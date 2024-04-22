# install dependencies
# $ pip install mysql-connector-python

# To start a temporary MySQL instance, you can use the following command:
# docker pull mysql
# docker run -it --rm --name temp-mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -p 3306:3306 mysql

# connect to mysql db using python.
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
