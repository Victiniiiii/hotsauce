import random

def simulate_game():
    drinks = [0, 0, 0, 0, 1]  # 0 represents a safe drink, 1 represents the hot sauce
    random.shuffle(drinks)  
    return drinks

def calculate_probabilities(num_trials):
    total_a = total_b = total_c = total_d = 0

    for _ in range(num_trials):
        drinks = simulate_game()

        # Player A
        if drinks[0] == 1:
            total_a += 1

        # Player B
        if drinks[1] == 1:
            total_b += 1

        # Player C
        if drinks[2] == 1:
            total_c += 1

        # Player D
        if drinks[3] == 1:
            total_d += 1

    prob_a = total_a / num_trials
    prob_b = total_b / num_trials
    prob_c = total_c / num_trials
    prob_d = total_d / num_trials

    return prob_a, prob_b, prob_c, prob_d

num_trials = 1000000
prob_a, prob_b, prob_c, prob_d = calculate_probabilities(num_trials)

print(f"Player A: {prob_a:.2%}")
print(f"Player B: {prob_b:.2%}")
print(f"Player C: {prob_c:.2%}")
print(f"Player D: {prob_d:.2%}")
