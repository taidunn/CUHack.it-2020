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
        self.name = header[1]
        self.hours = header[2]
        
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

def getPrereqs(name,number):
    info = []
    
    index = -1
    for i in range(0,len(departments)):
        if(departments[i][0] == name):
            index = i
            break
    c = departments[index][number]
    
    reqInfo = c.reqs_info
    if(reqInfo == "None"):
        return None
        
    reqInfo = "".join(reqInfo)
    
    
    
    
    ands = []
    ors = []
    grade = ""
    perm = ""
    
    lastDep = ""
    lastPrif = ""
    classTemp = []
    
    parts = reqInfo.replace(",", "")
    parts = parts.strip('.')
    parts = parts.split(' ')
    
    print("########")
    print(reqInfo)
    print(parts)
    print("------")
    
    for word in parts:
        if(word == ""):
            continue
        if(not isInt(word)):
            if(word == 'and'):
                if(lastPrif == 'or'):
                    ors.append(classTemp)
                    classTemp = []
                    lastDep = ''
                lastPrif = "and"
            elif(word == 'or'):
                if(lastPrif == 'and'):
                    ors.append(classTemp)
                    classTemp = []
                    lastDep = ''
                lastPrif = 'or'
            else:
                if(lastPrif == 'and'):
                    ands.append(classTemp)
                    classTemp = []
                    if(word == 'or'):
                        lastPrif = 'or'
                    else:
                        lastDep = word
                        classTemp.append(lastDep)
                elif(lastPrif == 'or'):
                    ors.append(classTemp)
                    classTemp = []
                    if(word == 'and'):
                        lastPrif = 'and'
                    else:
                        lastDep = word
                        classTemp.append(lastDep)
                elif(lastDep == ""):
                    lastDep = word
                    classTemp.append(lastDep)
                elif(lastDep == word):
                    continue
                else:
                    ands.append(classTemp)
                    classTemp = []
                    lastDep = word
                    classTemp.append(lastDep)
        else:
            classTemp.append(word)
        #print(lastDep)
        
        
    if(lastPrif == 'and'):
        ands.append(classTemp)
        classTemp = []
    elif(lastPrif == 'or'):
        ors.append(classTemp)
        classTemp = []
    else:
        ands.append(classTemp)
        classTemp = []
    
    print("------")
    print(ors)
    print(ands)
    print('\n')
    
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
   
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
            courses.append([c.department,c.courseNumber,c.name])
        else:
            for i in range(0,len(departments)):
                if(departments[i][0] == c.department):
                    departments[i][c.courseNumber] = c
                    courses.append([c.department,c.courseNumber,c.name])
                    break
                elif(i == len(departments)-1):
                    #print("appended")
                    departments.append([None]*1000)
                    departments[i+1][0] = c.department
                    departments[i+1][c.courseNumber] = c
                    courses.append([c.department,c.courseNumber])
                    
COM = "COM.csv"
PHIL = "PHIL.csv"
CLAR = "CLAR.csv"
AAS = "AAS.csv"
AERO = "AERO.csv"
APPL = "APPL.csv"
ARAB = "ARAB.csv"

read_csv(COM)
read_csv(PHIL)
read_csv(CLAR)
read_csv(AAS)
#read_csv(AERO)
#read_csv(APPL)
#read_csv(ARAB)

#print(departments[0])
#print(departments[1])
#print(departments[2])
#print(departments[3])
    

for i in range(0,150):
   #print(courses[i])  
   getPrereqs(courses[i][0],int(courses[i][1]))
#print(departments[4])
#print(departments[5])


       
