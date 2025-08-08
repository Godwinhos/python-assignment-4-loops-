i = 0
students =[]
while i <= 100:
    student ={
        "id": f"{i}",
        "name": f"student1{i}",
        "score": i % 100
    }
    students.append(student)
    i +=1
    
    print(student)
'''
i = 0
while i < len(students):
    student = students[i]
    print(f"ID: {student['id']}, Name: {student['name']}, Score: {student['score']}")
    i += 1

