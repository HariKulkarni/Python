#python prog to convert kilomiter to miles
def kilometer(km):
    conversion_ratio=0.621371
    miles=km*conversion_ratio
    print("the speed value of car in miles:",miles)
km=float(input("please enter the speed of car in kilometer as a unit: "))
kilometer(km)
