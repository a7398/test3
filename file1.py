import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

dates = ['17.03.2025', '18.03.2025', '19.03.2025', '20.03.2025', '21.03.2025']
dates = [mdates.datestr2num(date) for date in dates]
rates = [90.50, 91.25, 90.75, 92.00, 91.50]

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