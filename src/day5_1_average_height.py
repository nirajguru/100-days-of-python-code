from functools import total_ordering
# cacluate the average height of the people in the list using loops

student_heights = input("Input a list of student heights ").split()
# The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
#print(student_heights)
#average_height = sum(student_heights) / len(student_heights)
#print(average_height)


total_height = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_height += student_heights[n]
print (f"Average height: {total_height / len(student_heights)}")
