import random
import matplotlib.pyplot as plt

def monte_carlo_dice(num_simulations):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1
    
    probabilities = {}
    for sum_value, count in sums_count.items():
        probabilities[sum_value] = (count / num_simulations) * 100
    
    return probabilities

def analytical_probabilities():
    return {
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
        12: 2.78
    }

def main():
    num_simulations = 1000000
    
    monte_carlo_probs = monte_carlo_dice(num_simulations)
    analytical_probs = analytical_probabilities()
    
    print(f"{'Sum':<6} {'Monte-Carlo':<15} {'Analytical':<15} {'Difference':<10}")
    print("-" * 50)
    
    for sum_value in range(2, 13):
        mc_prob = monte_carlo_probs[sum_value]
        an_prob = analytical_probs[sum_value]
        diff = abs(mc_prob - an_prob)
        print(f"{sum_value:<6} {mc_prob:<15.2f}% {an_prob:<15.2f}% {diff:<10.2f}%")
    
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] for s in sums]
    an_values = [analytical_probs[s] for s in sums]
    
    plt.figure(figsize=(12, 6))
    
    x = range(len(sums))
    width = 0.35
    
    plt.bar([i - width/2 for i in x], mc_values, width, label='Monte-Carlo', alpha=0.8)
    plt.bar([i + width/2 for i in x], an_values, width, label='Analytical', alpha=0.8)
    
    plt.xlabel('Sum')
    plt.ylabel('Possibility (%)')
    plt.title(f'Comparasion (amount: {num_simulations:,})')
    plt.xticks(x, sums)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
