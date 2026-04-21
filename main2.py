# Task B1
driver_name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
fuel_consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

fuel_cost = (distance * fuel_consumption / 100) * fuel_price

if distance < 100:
    category = "Short trip"
elif 100 <= distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

print("=" * 30)
print("Driver:", driver_name)
print("Destination:", destination.upper())
print("Distance:", distance, "km")
print("Fuel cost:", fuel_cost, "KZT")
print("Category:", category)
print("=" * 30)

# Task B2
print("Cost Breakdown:")
for km in range(100, int(distance) + 1, 100):
    current_cost = (km * fuel_consumption / 100) * fuel_price
    print(km, "km->", current_cost, "KZT")

# Task B3
print("=" * 15)
print("Destination uppercase:", destination.upper())
print("Destination lowercase:", destination.lower())
print("Length:", len(destination))
print("Letter 'a' count:", destination.lower().count('a'))



