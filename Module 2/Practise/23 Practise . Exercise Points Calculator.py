run = int(input("Minutes spent running: "))
swm = int(input("Minutes spent swimming: "))
cyc = int(input("Minutes spent cycling: "))

r = run*5
s = swm*7
c = cyc*4
print("Points earned: ")
print(f"Running: {r} points")
print(f"Swmming: {s} points")
print(f"Cycling: {c} points")

print(f"Total pints: {r+s+c}")