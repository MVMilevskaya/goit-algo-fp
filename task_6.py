
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

def greedy_algorithm(items, budget):

    items_sorted = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        items_sorted.append(
            {"name": name, "cost": data["cost"], "calories": data["calories"], "ratio": ratio}
        )

    items_sorted.sort(key=lambda x: x["ratio"], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item in items_sorted:
        if total_cost + item["cost"] <= budget:
            chosen_items.append(item["name"])
            total_cost += item["cost"]
            total_calories += item["calories"]

    return chosen_items, total_cost, total_calories

def dynamic_programming(items, budget):

    names = list(items.keys())
    n = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(calories + dp[i - 1][w - cost], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    chosen_items = []
    total_cost = 0

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            chosen_items.append(name)
            w -= items[name]["cost"]
            total_cost += items[name]["cost"]

    total_calories = dp[n][budget]
    chosen_items.reverse()

    return chosen_items, total_cost, total_calories

if __name__ == "__main__":
    test_budget = 100

    print(f"=== Бюджет: {test_budget} ===")

    g_items, g_cost, g_cal = greedy_algorithm(items, test_budget)
    print("\n1. Жадібний алгоритм:")
    print(f"   Вибрані страви: {g_items}")
    print(f"   Загальна вартість: {g_cost}")
    print(f"   Загальні калорії: {g_cal}")

    dp_items, dp_cost, dp_cal = dynamic_programming(items, test_budget)
    print("\n2. Динамічне програмування:")
    print(f"   Вибрані страви: {dp_items}")
    print(f"   Загальна вартість: {dp_cost}")
    print(f"   Загальні калорії: {dp_cal}")