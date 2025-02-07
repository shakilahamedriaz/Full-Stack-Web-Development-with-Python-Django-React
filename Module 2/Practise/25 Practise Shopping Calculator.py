#all input
i = 1
total_sum = 0
while True:
    if i == 6:
        break
    items = float(input(f"Enter price for item {i}: "))
    i+=1
    total_sum += items


print("Receipt Summary: ")
round_total = round(total_sum)
print(f"Total (rounded): ${round_total}")
print(f"Total (exact): ${total_sum}")

avg_round = round_total / 5
avg_exact = total_sum / 5


print(f"Average per item (rounded): ${avg_round}")
print(f"Average per item (exact): ${avg_exact}")