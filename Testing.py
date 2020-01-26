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
        
        self.prerequisites = []
        
        self.info = info
        
        if("Requisites:" in self.info):
            self.reqs_info = self.initReqs_info()
        else:
            self.reqs_info = "None"
            
        if("Gen Ed:" in self.info):
            self.genEds = self.initGenEd_info()
        else:
            self.genEds = []
        
    def initReqs_info(self):
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
        
        
    def initGenEd_info(self):
        str = self.getSection('Gen Ed:')
        str = str.replace('Gen Ed:','')
        str = str.replace(' ','')
        str = str.replace('- Field Work.','')
        return str.split(',')
        
    def getSection(self, startWord):
        start = int(self.info.find(startWord))
        end = self.info.find('.', start)
        
        str = self.info[start:end+1]
        self.info = self.info[0:start] + self.info[end+1:]
        
        return str
    
    def fulfill(self, gens):
        for e in gens:
            if(e in self.genEds):
                return True
        return False
    
    def toString(self):
        return self.department + "-" + str(self.courseNumber) + self.name
##
##parses the info text for prereqs and sorts them based on departments and how the need to be taken
## 
def getPrereqs(name,number):
    info = []
    
    ##
    ##looks for the column in table
    ##
    index = -1
    for i in range(0,len(departments)):
        if(departments[i][0] == name):
            index = i
            break
    ##this is the course
    c = departments[index][number]
    
    ##
    ##gets info text
    ##
    reqInfo = c.reqs_info
    if(reqInfo == "None"):
        departments[index][number].prerequisites = None
        return
        
    reqInfo = "".join(reqInfo)

    ands = []
    ors = []
    
    lastDep = ""
    lastPrif = ""
    classTemp = []

    parts = reqInfo.replace(",", "")
    parts = parts.strip('.')
    parts = parts.split(' ')
    
    #print("########")
    #print(reqInfo)
    #print(parts)
    #print("------")
    
    ##
    ##Lots of mess
    ##
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
    
    #print("------")
    #print(ors)
    #print(ands)
    #print('\n')
    
    ##
    ##gets the actual course instances and stores them in list
    ##
    
    _ands = getCourses(ands)
    _ors = getCourses(ors)
    
    #print("ands : ")
    #print(_ands)
    
    ##
    ##updates the course in the table with prereqs
    ##
    if(len(_ands) == 0 and len(_ors) == 0):
        departments[index][number].prerequisites = None
    else:
        departments[index][number].prerequisites = [_ands,_ors]

##
##This takes in the parsed strings and creates a list of courses by looking in the talbe (using the info in the string list)
## 
def getCourses(ls):
    _ls = []
    for part in ls:
        if(len(part) == 0):
            continue
        department = part[0]
        if(department == "PERMS" or department == "C"):
            break
        index = -1
        for i in range(0,len(departments)):
            if(departments[i][0] == department):
                index = i
        for i in range(1,len(part)):  
           _ls.append(departments[index][int(part[i])])
    return _ls
    
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
                    courses.append([c.department,c.courseNumber,c.name])

##
##This takes a course department and number and returns the course from the talble
## 
def lookUpCourse(depart,number):
    index = -1
    for i in range(0,len(departments)):
        if(departments[i][0] == depart):
            index = i
            break
    return departments[index][number]

 
departments = []
departments.append([None]*1000)
courses = []

##
##some of these csvs are messed up
##    
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

gens = input("enter space delimited gen eds : ").split(" ")

selected = []

for e in courses:
    c = lookUpCourse(e[0],e[1])
    if(c.fulfill(gens)):
        print(c.toString())

input("....")
for e in courses:
    getPrereqs(e[0],e[1])

for e in courses:
    c = lookUpCourse(e[0],e[1])
    print(c.department + "  " + str(c.courseNumber) + " : " + c.name)
    
    if(not c.prerequisites == None):
        print("\n----Must----")
        for e in c.prerequisites[0]:
            if (not e == None):
                print(e.toString())
        print("----AtLeastOne----")
        for e in c.prerequisites[1]:
            if (not e == None):
                print(e.toString())
    print("\n\n")
    