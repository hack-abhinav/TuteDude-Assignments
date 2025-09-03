marks = {"Abhinav": 54 , "Pranit": 76 , "Sai": 93, "Manikanta": 45}
a = input("Enter Student's name: ")
if a in marks.keys():
    print(f"{a}'s marks: ", marks[a])
else:
    print("Student not found.")