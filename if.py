n=24
if n % 2 == 0:
    if n in range(2,5):
        print ("Not Weird")
    if n in range(6,20):
        print ("Weird")
    if n>20:
        print ("Not Weird")
else:
    print("Weird")