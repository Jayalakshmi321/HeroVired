stud1=int(input())
stud2=int(input())
stud3=int(input())
stud4=int(input())
stud5=int(input())
marks=[stud1,stud2,stud3,stud4,stud5]
for i in marks:
    print("entered marks:",i)
    if i<=40:
        continue
    print("marks of remaining students",i)
