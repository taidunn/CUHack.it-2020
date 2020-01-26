import csv

# permission of the instructor for students lacking the prerequisite.
# a grade of C or better is required in all prerequisite courses.
# a grade of C or better is required in COMP  116 or 401

class reqs:
    def __init__(ors, ands, froms):
        self.ors = ors
        self.ands = ands
        self.froms = froms
    
    def toString():
        return ""
        
class course:

    def __init__(self, header, info):
        header = header.split('.')
        self.department = header[0].split('  ')[0]
        self.courseNumber = int(header[0].split('  ')[1].strip('H'))
        self.name = header[2]
        self.hours = header[3]
        
        self.info = info
        
        if("Requisites:" in self.info):
            self.reqs_info = self.getReqs_info()
        else:
            self.reqs_info = "None"
            
        if("Gen Ed:" in self.info):
            self.genEd_info = self.getGenEd_info()
        else:
            self.genEd_info = []
        
    
    def getReqs_info(self):
        r = []
        
        str = self.getSection("Requisites:")
        str = str[str.find(',')+1:]
        reqs = str.split(';')
        for line in reqs:
            if("grade of" in line):
                grade = line[line.find('f ')+2:line.find('f ')+3]
                if('in both' in line.lower() or 'in all' in line.lower()):
                    r[len(r)-1] = r[len(r)-1] + " " + grade
                elif('is required in' in line.lower()):
                    r.append(line[line.find('in')+2:] + " " + grade)
                else:
                    r[len(r)-1] = r[len(r)-1] + " " + grade
            elif("permission of the instructor" in line.lower()):
                if(len(r) == 0):
                    r.append(line[0:line.find("permission")] + " PERM")
                else:
                    r[len(r)-1] = r[len(r)-1] + " PERMS"
            else:
                r.append(line)
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
        



departments = []
departments.append([None]*1000)
courses = []

def stripNonAscii(str):
    return ''.join([i if ord(i) < 128 else ' ' for i in str])
    
def read_csv(path):
    f = open(path)
    c = 0
    
    for row in csv.reader(f):
        if(c == 0):
            c += 1
            continue
        
        c = course(stripNonAscii(row[0]),stripNonAscii(row[1]))
        if (departments[0][0] == None):
            departments[0][c.courseNumber] = c
            departments[0][0] = c.department
            courses.append[c.department,c.courseNumber]
        else:
            for i in range(0,len(departments)):
                if(departments[i][0] == c.department):
                    departments[i][c.courseNumber] = c
                    courses.append[c.department,c.courseNumber]
                    break
                elif(i == len(departments)-1):
                    print("appended")
                    departments.append([None]*1000)
                    departments[i+1][0] = c.department
                    departments[i+1][c.courseNumber] = c
                    courses.append[c.department,c.courseNumber]

                    
COM = "COM.csv"
PHIL = "PHIL.csv"
CLAR = "CLAR.csv"

read_csv(COM)
read_csv(PHIL)
read_csv(CLAR)

print(departments[0])
print(departments[1])
print(departments[2])


       
