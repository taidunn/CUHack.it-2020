import csv

# permission of the instructor for students lacking the prerequisite.
# a grade of C or better is required in all prerequisite courses.
# a grade of C or better is required in COMP  116 or 401

class req:
    def __init__(self, department, reqs, rules):
        self.department = department
        self.reqs = reqs
        self.rules = rules
    
    def toString():
        return ""
        
class course:

    def __init__(self, header, info):
        header = header.split('.')
        self.department = header[0].split('  ')[0]
        self.courseNumber = header[0].split('  ')[1]
        self.name = header[2]
        self.hours = header[3]
        
        self.info = info
        
        if("Requisites:" in self.info):
            self.getReqs_info()
        else:
            self.getReqs_info = []
            
        if("Gen Ed:" in self.info):
            self.genEd_info = self.getGenEd_info()
        else:
            self.genEd_info = []
            
    def getReqs_info(self):
        r = []
        
        str = self.getSection("Requisites:")
        str = str[str.find(',')+1:]
        reqs = str.split(';')
        print("-----------------------------------")
        for line in reqs:
            if("a grade of" in line.lower()):
                grade = line[line.find("of ")+3:line.find("of ")+4]
                if(not "or better in" in line.lower()):
                    r.append(line[line.find(" in")+3:] + " " + grade)
                else:
                    r[len(r)-1] = r[len(r)-1] + " " + grade
            elif("permission of the instructor" in line.lower()):
                r[len(r)-1] = r[len(r)-1] + " PERM"
            else:
                print(r)
                r.append(line)
        print("-----------------------------------")
        return r
        
    def getGenEd_info(self):
        genEds = []
        return genEds
        
    def getSection(self, startWord):
        start = int(self.info.find(startWord))
        end = self.info.find('.', start)
        
        str = self.info[start:end+1]
        self.info = self.info[0:start] + self.info[end+1:]
        
        return str
        
def stripNonAscii(str):
    return ''.join([i if ord(i) < 128 else ' ' for i in str])

f = open("Data.csv")

courses = []
c = 0
for row in csv.reader(f):
    if(c == 0):
        c += 1
        continue
    
    courses.append(course(stripNonAscii(row[0]),stripNonAscii(row[1])))
    
    
    
    
    
    