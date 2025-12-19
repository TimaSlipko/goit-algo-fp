def greedy_algorithm(items, budget):
    ratio_items = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        ratio_items.append((name, info["cost"], info["calories"], ratio))
    
    ratio_items.sort(key=lambda x: x[3], reverse=True)
    
    res = {}
    total_cost = 0
    total_calories = 0
    
    for name, cost, calories, ratio in ratio_items:
        if total_cost + cost <= budget:
            res[name] = 1
            total_cost += cost
            total_calories += calories
    
    return res, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    res = {}
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            res[name] = 1
            b -= items[name]["cost"]
    
    return res, dp[n][budget]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    budget = 100
    
    greedy_res, greedy_cal = greedy_algorithm(items, budget)
    print(f"greedy: {greedy_res}, calories: {greedy_cal}")
    
    dynamic_res, dynamic_cal = dynamic_programming(items, budget)
    print(f"dynamic: {dynamic_res}, calories: {dynamic_cal}")


if __name__ == '__main__':
    main()