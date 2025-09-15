def person_details():
    person=[]
    n=int(input("enter the no of person:"))
    for i in range(0,n):
        name=input("enter:")
        age=int(input("enter the age:"))
        disease=input("enter the disease:")
        person.append({'name':name, 'age':age,'disease':disease})
    return person
def search(a):
    dis=input("enter disease:")
    f=False
    for i in a:
        if i['disease'] ==dis:
            print(f"Patients with Flu:{i['name']}")
            f=True
    if not f:
        print("no patient with that disease")


a=person_details()
print(a)
search(a)