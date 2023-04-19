#tp = ticket price , hm = members
tp = int(input("Ticket Price :- "))
hm=int(input("How many Members :- "))
total = 0
#your code goes here
i = 0
while i < hm:
    age = int(input("Age of the person :- "))
    
    i=i+1
    print(i , "person age is ","(",age,')')
    if age <= 3:
        continue 
    total += tp
print('total Members is',i,"Total Price is",total ,'Rs')
      