import random
student_list = []
max = int(input("끝번호는? : "))
student_list = list(range(1, max+1))
while True:
    exclude_number_string = input("제외할 번호는? : ")
    if exclude_number_string  == "":
        break
    student_list.remove(int(exclude_number_string))
length = len(student_list)
position = random.sample(range(1, length+1), length)
for i, value in enumerate(position):
    print(i+1, "\t",value)
