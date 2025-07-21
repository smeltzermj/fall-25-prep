# converter.py

KM_PER_MILE = 1.60934

def miles_to_km(miles: float) -> float:
    return miles * KM_PER_MILE

def km_to_miles(km: float) -> float:
    return km / KM_PER_MILE

choice = input("Convert (1) miles→km or (2) km→miles? ")
value = float(input("Enter the distance: "))

if choice == "1":
    result = miles_to_km(value)
    unit_in, unit_out = "mi", "km"
elif choice == "2":
    result = km_to_miles(value)
    unit_in, unit_out = "km", "mi"
else:
    print("Invalid choice.")
    exit(1)

print(f"{value:.2f} {unit_in}  =  {result:.2f} {unit_out}")
