from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import matplotlib.pyplot as plt


driver = webdriver.Chrome()

# Открытие страницы
url = "https://www.divan.ru/category/divany "
driver.get(url)

# Ждём загрузки товаров
time.sleep(5)

# Парсим цены
prices = []
elements = driver.find_elements(By.XPATH, '//span[@data-testid="price"]')

for el in elements:
    try:
        price_text = el.text.replace(' ', '').replace('руб.', '')
        if price_text.isdigit():
            prices.append(int(price_text))
    except Exception as e:
        print(f"Ошибка при обработке: {e}")

# Закрываем браузер
driver.quit()

# Сохраняем в CSV
df = pd.DataFrame(prices, columns=["Price"])
df.to_csv("divan_prices.csv", index=False)
print("✅ Цены успешно сохранены в файл divan_prices.csv")

# Вычисляем среднюю цену
average_price = df["Price"].mean()
print(f"💰 Средняя цена дивана: {round(average_price)} руб.")

# Гистограмма цен
plt.figure(figsize=(10, 6))
plt.hist(df["Price"], bins=30, color='skyblue', edgecolor='black')
plt.title("Распределение цен на диваны")
plt.xlabel("Цена (руб.)")
plt.ylabel("Количество")
plt.grid(True, axis='y', alpha=0.75)
plt.show()