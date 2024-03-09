import time


def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    coins_count = {}

    for denomination in denominations:
        count = amount // denomination
        if count > 0:
            coins_count[denomination] = count
        amount %= denomination

    return coins_count


def find_min_coins(amount):
    denominations = [1, 2, 5, 10, 25, 50]
    min_coins_count = [float('inf')] * (amount + 1)
    last_coin_used = [0] * (amount + 1)
    min_coins_count[0] = 0

    for coin in denominations:
        for current_amount in range(coin, amount + 1):
            if min_coins_count[current_amount - coin] + 1 < min_coins_count[current_amount]:
                min_coins_count[current_amount] = min_coins_count[current_amount - coin] + 1
                last_coin_used[current_amount] = coin

    coins_used = {}
    current_amount = amount
    while current_amount > 0:
        coin = last_coin_used[current_amount]
        coins_used[coin] = coins_used.get(coin, 0) + 1
        current_amount -= coin

    return coins_used


# Порівняння часу виконання жадібного алгоритму
start_time = time.time()
greedy_result = find_coins_greedy(9584)
greedy_execution_time = time.time() - start_time
print(f"Результат жадібного алгоритму: {greedy_result}")
print(f"Час виконання жадібного алгоритму: {greedy_execution_time:.6f} секунд")

# Порівняння часу виконання алгоритму динамічного програмування
start_time = time.time()
dynamic_programming_result = find_min_coins(9584)
dynamic_programming_execution_time = time.time() - start_time
print(
    f"Результат алгоритму динамічного програмування: {dynamic_programming_result}")
print(
    f"Час виконання алгоритму динамічного програмування: {dynamic_programming_execution_time:.6f} секунд")
