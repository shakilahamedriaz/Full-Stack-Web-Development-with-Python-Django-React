#calculate total cost
pencils = 5
pencil_price = 0.75

total = pencils * pencil_price
print(f"Total cost of the pencils: $ {total} only")

#output: 3.75


#Convert minutes to hours and minutes
total_minutes = 145
hours = total_minutes // 60   #as integer division
minutes = total_minutes % 60  #as modulus , take reminder of the diviosn

print(f"{total_minutes} minutes is {hours}h {minutes}m")
#output: 145 minutes is 2h 25m