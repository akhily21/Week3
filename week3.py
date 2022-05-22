class Students:
    student_details={
    "Ron": 10,
    "Jack": 9,
    "Jose": 5    
    }
    def search(self,name):
        if self.student_details.get(name)==None:
            print("The student does not exist")
        else:
            print("The student grade is ",self.student_details[name])

    def add(self, name, grade):
        student.student_details.update({name: grade})
        print("Student added successfully. Updated list is ", student.student_details)

    def delete(self,name):
           student.student_details.pop(name)
           print("Student deleted successfully. Updated list is ", student.student_details)

student=Students()


while(1):  
#Student Grade search
    s=input("Do you want to search a student's grade?: Y or N")
    if(s=='Y'):
        name=input("Enter the name of the student")
        student.search(name)
    user_choice=input(" Do you wish to add a student? Enter A\n Do you want to delete a student? Enter D\n Do you want to update a student's grade? Enter U")

#Add or Delete records
    if(user_choice=='A'):
        name=input("Enter the name of the student you wish to add")
        grade=input("Enter the student's grade")
        student.add(name, grade)
    elif(user_choice=='D'):
        name=input("Enter the name of the student yu wish to delete")
        student.delete(name)
    elif(user_choice=='U'):
        name=input("Enter the name of the student you wish to update")
        grade=input("Enter the student's grade")
        student.add(name, grade)
    else:
        print('Invalid Choice')
