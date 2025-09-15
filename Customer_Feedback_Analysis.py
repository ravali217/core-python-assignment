def details():
    print(" ```python")
    ratings = [5, 4, 2, 5, 2, 4, 1, 5]
    
    return ratings
def pos_rating(a):
    count=0
    for i in a:
        if i>=4:
            count+=1
    total=(count/len(a))*100
    print(" ```")
    print(f"positive feedback: {total}%")
    print(" ```")

a=details()
print(f"{a} \n``` ")
pos_rating(a)
