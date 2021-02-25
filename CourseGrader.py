
class student():
    def __init__(self, FName, LName, GradeList):
        self.FirstName = FName
        self.LastName = LName
        self.GradesList = GradeList

    def gradeSort(self):
        fullGradeString = ""
        for grade in self.GradesList:
            fullGradeString += (str(grade) + ", ")
        return fullGradeString

    def get_average(self):
        return (sum(self.GradesList) / len(self.GradesList))

    def get_letter(self):
        userGrade = self.get_average()
        if userGrade < 60:
            return "F"
        elif userGrade > 59 and userGrade < 70:
            return "D"
        elif userGrade > 69 and userGrade < 80:
            return "C"
        elif 90 > userGrade > 79:
            return "B"
        elif 100 > userGrade > 89:
            return "A"
        else:
            return "A+"

    def __str__(self): 
        return  self.FirstName + " " + self.LastName + " " + str(self.gradeSort()) + " -- " + str(self.get_letter())



inputFile = open("grades.txt", "r")
input = inputFile.readlines()
for i in range(len(input)):
    input[i] = input[i].strip()

totalStudents = input[0]
input.remove(input[0])

for i in range(len(input)):
    try:
        input[i] = int(input[i])
    except:
        input[i] = str(input[i])
        
studentInfo = []
AllStudentsInfo = []
AllGrades = []

for i in range(len(input)):
    if input[i] != 0 and (isinstance(input[i], int)) == True:
        studentInfo.append(input[i])
 
    elif input[i] == 0:
        for i in range(1):
            AllStudentsInfo.append(studentInfo)
        studentInfo = []


for i in range(len(AllStudentsInfo)):
    list = AllStudentsInfo[i]
    list.sort()
    AllStudentsInfo[i] = list


AllGrades = []
AllNames = []
for i in range(len(input)):
    if input[i] != 0 and (isinstance(input[i], int)) == True:
        AllGrades.append(input[i])
    elif input[i] != 0 and (isinstance(input[i], int)) == False:
        AllNames.append(input[i])


firstNames = []
lastNames = []
for i in range(len(AllNames)):
    parts = AllNames[i].split()
    firstNames.append(parts[0])
    lastNames.append(parts[1])



for i in range(len(AllNames)):
    print(student(firstNames[i], lastNames[i], AllStudentsInfo[i]))

AllGrades.sort()
lowestGrade = min(AllGrades)
highestGrade = max(AllGrades)
AverageGrade = (sum(AllGrades) / len(AllGrades))
maxSpot = 0
for i in range(len(AllNames)):
    if len(AllNames[i]) > len(AllNames[maxSpot]):
        maxSpot = i
longestName = AllNames[maxSpot]
outputFile = open("summary.txt", "w")
outputFile.write("Number of students: " + str(totalStudents) + "\n")
outputFile.write("Average grade: " + str(AverageGrade) + "\n")
outputFile.write("Highest grade: " + str(highestGrade) + "\n")
outputFile.write("Lowest grade: " + str(lowestGrade) + "\n")
outputFile.write("Student with longest name: " + str(longestName) + "\n")
outputFile.close()