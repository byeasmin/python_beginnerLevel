available=int(input("Available candies are : "))
x=int(input("How many candies do you want to buy ? "))
i=1
while i<=x:
    if i>available:
        print("out of stock")
        break
    print("candy")
    i=i+1




'''    
output_type_1:
Available candies are : 5
How many candies do you want to buy ? 4
candy
candy
candy
candy
'''




'''
output_type_2:
Available candies are : 5
How many candies do you want to buy ? 7
candy
candy
candy
candy
candy
out of stock
'''

