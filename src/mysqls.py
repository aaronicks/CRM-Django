import mysql.connector


databases = mysql.connector.connect(
	host = 'localhost',
	user = 'admin',
	passwd = 'admin',
	)

objectcursor = databases.cursor()

objectcursor.execute('CREATE DATABASE elderco')
print('All Done!')