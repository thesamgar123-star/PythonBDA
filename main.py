# a) Input & Variables
driver_name = input("Enter driver name: ")
distance = float(input("Enter distance (km): "))
fuel_consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

# b) Calculations
litres_needed = distance * fuel_consumption / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / distance

# c) Formatted Output
print("=" * 30)
print("ROAD TRIP SUMMARY")
print("-" * 30)
print("Driver:", driver_name)
print("Distance:", distance, "km")
print("Consumption:", fuel_consumption, "L/100km")
print("Fuel price:", fuel_price, "KZT/L")
print("Litres needed:", litres_needed, "L")
print("Fuel cost:", fuel_cost, "KZT")
print("Cost per km:", cost_per_km, "KZT")
print("=" * 30)

# d) Comparison
print("Trip longer than 300 km:", distance > 300)
print("Fuel cost above 5000 KZT:", fuel_cost > 5000)
