# try & except used to detect errors when user enters weight of the package
try:
    weight = float(input("Enter the weight of your package in kg: "))
except ValueError:
    print("Invalid input. Please input a valid numeric weight")
    exit(1)

# ground shipping costs
if weight <= 2:
    ground_shipping = 1.50 * weight + 20.00
elif 2 < weight <= 6:
    ground_shipping = 3.00 * weight + 20.00
elif 6 < weight <= 10:
    ground_shipping = 4.00 * weight + 20.00
else:
    ground_shipping = 4.75 * weight + 20.00

print("Ground shipping:", ground_shipping)

# drone shipping costs
if weight <= 2:
    drone_shipping = 4.50 * weight
elif 2 < weight <= 6:
    drone_shipping = 9.00 * weight
elif 6 < weight <= 10:
    drone_shipping = 12.00 * weight
else:
    drone_shipping = 14.25 * weight

print("Drone shipping:", drone_shipping)

# ground shipping premium cost
ground_shipping_premium = 125.00
print("Ground shipping premium:", ground_shipping_premium)

# determine the cheapest shipping
if ground_shipping < drone_shipping and ground_shipping < ground_shipping_premium:
    cheapest_shipping = "ground shipping"
    cheapest_cost = ground_shipping
elif drone_shipping < ground_shipping and drone_shipping < ground_shipping_premium:
    cheapest_shipping = "drone shipping"
    cheapest_cost = drone_shipping
else:
    cheapest_shipping = "ground shipping premium"
    cheapest_cost = ground_shipping_premium

print(f"The cheapest shipping method is {cheapest_shipping}, and costs £ {cheapest_cost}")
