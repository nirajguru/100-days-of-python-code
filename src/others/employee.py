# class Employee:

#     name = "Niraj"
#     grade = "A" #class attributes
    
#     def hasAchievedTarget(self):
#         #self is used to access the attributes of class
#         if self.finished_course >= 2:
#             print("target achieved")
#         else:
#             print("not achieved")


# Employee.grade = "B"
# niraj_emp = Employee()
# print(niraj_emp.grade)


class Employee:
    def my_func(self):
        self.hey()

    def hey(self):
        print("hey there")

niraj = Employee()
niraj.my_func()  # This is same as 
Employee.my_func(niraj)