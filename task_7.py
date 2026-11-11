import random

def monte_carlo_dice_simulation(num_simulations=100000):

    counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        counts[total] += 1

    probabilities = {}
    for total, count in counts.items():
        probabilities[total] = (count / num_simulations) * 100

    return probabilities

analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def print_comparison_table(mc_probs):
    print(
        f"{'Сума':<6} | {'Монте-Карло (%)':<18} | {'Аналітична (%)':<15} |"
        f" {'Різниця (%)':<10}"
    )
    print("-" * 60)

    for sum_value in range(2, 13):
        mc_val = mc_probs[sum_value]
        an_val = analytical_probabilities[sum_value]
        diff = abs(mc_val - an_val)
        print(
            f"{sum_value:<6} | {mc_val:<18.2f} | {an_val:<15.2f} |"
            f" {diff:<10.2f}"
    )

if __name__ == "__main__":
    n_sims = 100000
    print(f"Запуск симуляції методом Монте-Карло ({n_sims:,} кидань)...\n")

    mc_results = monte_carlo_dice_simulation(n_sims)
    print_comparison_table(mc_results)