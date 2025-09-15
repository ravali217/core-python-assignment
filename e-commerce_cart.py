def cal(cart_items):
    if not cart_items:
        print("cart is empty")
        return 0
    sum=0
    for i in cart_items.values() :
        sum+=i
    if len(cart_items)>=5:
       dis=sum*0.1
       sum=sum-dis
       print(sum)
    else:
       
        print(sum)
a=int(input("enter the number of items:"))
cart_items={}
for i in range(a):
    cname=input()
    cprice=int(input())
    cart_items[cname]=cprice
print(cart_items)
cal(cart_items)          



