def student_details():
    st={}
    for s in range(3):
        name=input("enter:")
        marks=list(map(int,input().split(" ")))
        st[name]=marks
    return st
def display(student):
    print("{",end=" ")
    count=0
    for name,marks in student.items():
        count+=1
        print(f"{name}:{marks}",end=" ")
        if count!=len(student):
            print(",",end=" ")
    print("}")
def avg(student):
        
    averages={}
    count=0

    print("\n{",end=" ")
    for name,marks in student.items():
        avg=sum(marks)/len(marks)
        averages[name]=avg
        print(f"{name}:{avg:.2f}",end=" ")
        count+=1
        if count!=len(student):
            print(",",end=" ")
    print(" }")
    return averages
def max_avg(averages):
    max_avg1=max(averages.values())
    for name,avg in averages.items():
        if avg==max_avg1:
            print(f"{name}:{max_avg1:.2f}")


student=student_details()
display(student)
averages=avg(student)
max_avg(averages)




        
  