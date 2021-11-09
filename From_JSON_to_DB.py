import pymysql
import json
from Config import user, host, password

try:
	connection = pymysql.Connect(
		host=host,
		port=3306,
		user=user,
		password=password,
		cursorclass=pymysql.cursors.DictCursor
	)
	MySQL = connection.cursor()
	print('Connection - OK')
except Exception as ex:
	print('Connection - fail')
	print(ex)
# with MySQL:
# 	MySQL.execute('TRUNCATE TABLE Food_info.Food_info')
# with MySQL:
# 	MySQL.execute('CREATE TABLE Food_info.Food_info(Title varchar(255),'
# 				  ' Weight int(16) NOT NULL, '
# 				  'Calories int(16) NOT NULL, '
# 				  'Proteins float(16) NOT NULL, '
# 				  'Fats float(16) NOT NULL, '
# 				  'Carbohydrates float(16) NOT NULL);'
# 				  )
#
# for num in range(0, 53):
# 	f = f'Data_{num}.json'
# 	with open(f, 'r', encoding='utf-8') as json_f:
# 		python_obj = json.load(json_f)
# 		for elem in python_obj:
# 			Title1 = elem.get('Title')
# 			Weight1 = elem.get('Weight')
# 			Calories1 = elem.get('Calories')
# 			Proteins1 = elem.get('Proteins')
# 			Fats1 = elem.get('Fats')
# 			Carbohydrates1 = elem.get('Carbohydrates')
# 			MySQL.execute("insert into Food_info.Food_info(Title, Weight, Calories, Proteins, Fats, Carbohydrates) "
# 						  "value(%s, %s, %s, %s, %s, %s)",
# 						  (Title1, Weight1, Calories1, Proteins1, Fats1, Carbohydrates1))
# 			connection.commit()
with MySQL:
	MySQL.execute('Select * From Food_info.Food_info;')
	for row in MySQL.fetchall():
		print(row)