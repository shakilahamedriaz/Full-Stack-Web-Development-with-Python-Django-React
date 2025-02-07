dis = int(input("Enter distance (km): "))

hr = input("Enter hours: ")
mn = input("Enter minutes: ")


time_taken = (int(hr) * 60) + int(mn)
new_time =  time_taken / 60


print(f"Time taken: {new_time} hurs")
print(f"Average speed: {dis/new_time} km/h")