import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

#  Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Функція цілі
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
water = 100
sugar = 50
lemon_juice = 30
fruit_puree = 40

# Додавання обмежень
model += 2 * lemonade + fruit_juice <= water, "Water"
model += lemonade <= sugar, "Sugar"
model += lemonade <= lemon_juice, "Lemon_Juice"
model += 2 * fruit_juice <= fruit_puree, "Fruit_Puree"

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Лимонад: {lemonade.varValue}")
print(f"Фруктовий сік: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue}")