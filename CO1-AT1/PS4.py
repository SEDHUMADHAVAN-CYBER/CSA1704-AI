cabs = {
    "Micro": 120,
    "Mini": 160,
    "Sedan": 250,
    "Prime": 350,
    "Shared": 90
}

source = input("Enter Source : ")
destination = input("Enter Destination : ")

print("\nAvailable Cabs")

for cab in cabs:
    print(cab, "- ₹", cabs[cab])

choice = input("\nSelect Cab : ")

if choice in cabs:
    print("\nBooking Successful")
    print("Source :", source)
    print("Destination :", destination)
    print("Cab :", choice)
    print("Fare : ₹", cabs[choice])
else:
    print("Cab Not Available")