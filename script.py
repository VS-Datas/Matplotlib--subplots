import codecademylib
from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)
plt.plot(temperature, months, color= 'yellow')
plt.title('Temperature vs Months')
plt.show()

plt.subplot(1, 2, 2)
plt.plot(flights_to_hawaii, temperature, marker= 's', color= 'green')
plt.title('Temperature vs Flights to Hawaii')
plt.show()






