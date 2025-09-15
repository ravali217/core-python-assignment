def add(ele):
    initial_menu.append(ele)
    print(f"\n add_item ={ele}")
    print(initial_menu)
def remove(ele):
    if ele in initial_menu:
        initial_menu.remove(ele)
        print(f"remove_item = {ele }")
        print(initial_menu)
    else:
        print(f"{ele} not found in menu. Cannot remove.")
def check(ele):
    if ele in initial_menu:
        print(f"check_item:{ele} is avaliable")
    else:
        print(f"{ele} not found in menu.")


initial_menu=[]
for i in range(4):
    item_name=input("enter the items:")
    initial_menu.append(item_name)
for i in initial_menu:
    print(i, end=" ")

add("tacos")
remove("salad")
check("pizza")




