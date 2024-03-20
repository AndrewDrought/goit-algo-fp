import random
import pandas as pd

# Кількість кидків
num_rolls = 1000000

# Створюємо словник для зберігання результатів
results = {i: 0 for i in range(2, 13)}

# Симулюємо кидки кубиків
for _ in range(num_rolls):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    results[roll1 + roll2] += 1

# Обчислюємо ймовірності
probabilities = {i: results[i] / num_rolls for i in range(2, 13)}

# Виводимо результати в форматі таблиці
df = pd.DataFrame(list(probabilities.items()), columns=['Сума', 'Ймовірність'])
df['Ймовірність'] = df['Ймовірність'].apply(lambda x: f"{x * 100:.2f}%")
print(df.to_string(index=False))
