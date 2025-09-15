def total():
    total_seats=int(input("enter the nnumber of seats:"))
    return total_seats
def booked_seats(t):
        book=[]
        bookedseats=list(map(int,input().split()))
        for i in bookedseats:
            if (i<1 or i>t):
                print("invalid out of range")
                exit()
            else:
                 book.append(i)

        return book
        
             
def book_seat(t,b):
    to_book=[]
    bseat=list(map(int,input().split()))
    for i in bseat:
        if (i<1 or i>t):
             print("out of range")
        elif i in b:
             print(("is booked"))
        else:
             to_book.append(i)
             
    return bseat
def cancel(t,b):
    c=list(map(int,input().split()))
    for i in c:
        if i in b:
            b.remove(i)
            print(f"seat{i}is cancelled")
        else:
            print(f"ele {i}not fount")
    return b
def avaliable(b):
     ava=[i for i in range(1,t+1) if i not in b]
     return ava
    
t=total()
b=booked_seats(t)
print(b)
newseat=book_seat(t,b)

b.extend(newseat)
print(sorted(b))
u=cancel(t,b)
print(u)
a=avaliable(b)
print(a)


