#write a program to decide which is cheaper approach to go from ahmedabad to delhi.

dis_km=int(input("Enter distance from ahmedabad to delhi(in km):"))
mileage=int(input("Enter car mileage (km per litre):"))
petrol_rice=int(input("Enter petrol price per litre:"))
train_fare=int(input("Enter 1st class train fare :"))

fual_required=dis_km/mileage
car_cost=fual_required*petrol_rice

print("Travel cost details")
print("Car Travel cost",car_cost)
print("Train Travel cost",train_fare)

if car_cost<train_fare:
    print("car travel is cheaper than train travel")
else:
    print("train travel is cheaper than car travel")