#print()
temperature = int(input("key in the temperature "))
if temperature > 30:
    print("it's a hot day!")
    print("drink lot of water")
elif temperature > 20:#(20,30]
    print("it's a nice day!")
elif temperature > 10: #(10,20]
    print ("it's a cold day!")
else:
    print("it's cold!!!")    
print("done")

weight = int(input("Enter weight: "))
unit = input("(K)g or (L)bs")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: "+str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs: "+ str(converted))

