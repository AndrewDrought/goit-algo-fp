items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    chosen_items = []
    total_cost = 0

    for item in sorted_items:
        cost = item[1]['cost']
        if total_cost + cost <= budget:
            chosen_items.append(item[0])
            total_cost += cost

    return chosen_items


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    chosen = [0] * (budget + 1)

    for i in range(1, budget + 1):
        for item, info in items.items():
            cost = info['cost']
            if cost <= i:
                val = dp[i - cost] + info['calories']
                if val > dp[i]:
                    dp[i] = val
                    chosen[i] = item

    result = []
    i = budget
    while i > 0:
        result.append(chosen[i])
        i -= items[chosen[i]]['cost']

    return result


print(greedy_algorithm(items, 100))
print(dynamic_programming(items, 100))
