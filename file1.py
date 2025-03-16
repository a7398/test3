import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(dates, rates, 'bo-', label='Курс USD')
plt.title('Курс USD по датам')
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()  
