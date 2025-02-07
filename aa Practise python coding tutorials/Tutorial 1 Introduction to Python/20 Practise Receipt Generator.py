store_name = input("Enter store name: ")

item_1 =   input("Enter item 1: ")
price_1 = float(input("Enter price 1: "))

item_2 =   input("Enter item 2: ")
price_2 =  float(input("Enter price 2: "))

item_3 =    input("Enter item 3: ")
price_3 =   float(input("Enter price 3: "))


#print here

print("=" * 30)
print(f"{' ' * 9} {store_name}  {' ' * 9 }")
print("=" * 30)

print(f"{item_1}          ${price_1}")
print(f"{item_2}          ${price_2}")
print(f"{item_3}          ${price_3}")

sum = price_1 + price_2 + price_3
print('- '*16)
print(f"Total:          ${sum}")
print("=" * 30)