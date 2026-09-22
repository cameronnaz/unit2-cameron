""" has_key = False
is_magic = True
if has_key or is_magic:
    print("Enter Castle")
else:
    print("cannot enter") """

#when there is an "or" in between has_key  and is_magic, then only one of them has to be true in order for it to pront enter castle

""" has_key = True
is_magic = True
if has_key and is_magic:
    print("Enter Castle")
else:
    print("cannot enter")
 """
#when there is "and" in between them, both of them need to be true in order for it to say enter castle

""" rain = False
if rain == True:
    print("Bring Umbrella")
else:
    print("Dont bring umbrella") """

#since rain = false in this one, it is not true so it prints dont bring umbrella

""" rain = True 
if rain == True:
    print("Bring Umbrella")
else:
    print("Dont bring umbrella") """

#since rain = true, it prints to bring the umbrella

age = 66
if age > 65:
    print("Senior Citizen")
elif age > 18:
    print("Adult")
else:
    print("Child")