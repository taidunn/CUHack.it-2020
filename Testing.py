import csv

class reqs:
    def __init__(self, department, reqs, rules):
        self.department = department
        self.reqs = reqs
        self.rules = rules
    
    def toString():
        return ""
        
class course:

    def __init__(self, header, info):
        header = unicode(header, "utf-8")
        header = header.split('.')
        header[0] = header[0].replace(u'\xa0', u' ')
        
        self.department = header[0].split(' ')[0]
        self.courseNumber = header[0].split(' ')[1]
        self.name = header[2]
        self.hours = header[3]
        
        self.info = info
        
        if("Requisites:" in info):
            self.requisites = self.getReqs()
        else:
            self.requisites = []
        #if("Gen Ed:" in info):   
        #    self.genEd = self.getGenEd()
        #else:
        #    self.genEd = []
        
        
    
    def getReqs(self):
        r = []
        
        str = self.getSection("Requisites:")
        str = str[str.find(','):]
        str.split(';')
        print(str)
        return r
        
    def getGenEd(self):
        genEds = []
        return genEds
        
    def getSection(self, startWord):
        start = int(self.info.find(startWord))
        end = self.info.find('.', start)
        
        str = self.info[start:end+1]
        self.info = self.info[0:start] + self.info[end+1:]
        
        return str

f = open("Data.csv")

courses = []
c = 0
for row in csv.reader(f):
    if(c == 0):
        c += 1
        continue
        
    courses.append(course(row[0],row[1]))
    
    
    
    
    
    