import csv      
class Courses:
	def __init__(self, name, info):
		self.name = name
		self.info = info

f = open('Data.csv')
csv_f = csv.reader(f)

list = []
for row in csv_f:
	list.append( Courses(row[0], row[1]) ) 
	
print(len(list))
print(list[1].info)
