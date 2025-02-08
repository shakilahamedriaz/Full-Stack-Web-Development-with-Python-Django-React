def calculate_score(hits, misses):
    score = (hits * 100) - (misses * 50)
    return score



hits = int(input("Enter player hits : "))
misses = int(input("Enter player misses : "))

playerScore = calculate_score(hits, misses)
print(f"Your Score: ", playerScore)