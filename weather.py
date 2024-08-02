tempeture = 50

if tempeture > 80 or tempeture < 60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors")
 
tempeture = 75
forecast = "sunny"

if tempeture < 80 and forecast != "rainy":
    print("Go outside")
else:
    print("Stay inside")

if not forecast == "rainy":
    print("Go outside 2")
else:
    print("Stay inside")

raining = True

if raining:
    print("Go outside 3")
else:
    print("Stay inside")