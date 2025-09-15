def details():
    t=[]
    print(" ```python")
    for i in range(3):
        trip=int(input("enter:"))
        t.append(trip)
    return t
def output(a):
    # tr=[]
    sum=0
    num=1
    for i in a:
        t=(i*10)+50
        print(f"trip {num} : {t}")
        sum=sum+t
        num+=1
        # tr.append(t)
    return sum 
    
a=details()
print(f"{a} ```")
b=output(a)
print(f"total fare:{b}")