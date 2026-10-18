from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

# Establish constants

T_LOW = np.arange(1, 99)
T_HIGH = np.arange(99, 374)  # stored as numpy arrays so vector calculation can be done

A_LOW = 8.07131
B_LOW = 1730.63
C_LOW = 233.426

A_HIGH = 8.13019
B_HIGH = 1810.94
C_HIGH = 244.486

P_ATM = 760

# Calculation

P_LOW = 10**(A_LOW - B_LOW / (T_LOW + C_LOW))
P_HIGH = 10**(A_HIGH - B_HIGH / (T_HIGH + C_HIGH))

oneATMTemp = np.interp(P_ATM, P_HIGH, T_HIGH)

# Plotting the pressure against temperature and showing the interpolation

plt.plot(T_LOW, P_LOW, color="blue")
plt.plot(T_HIGH, P_HIGH, color="red")

plt.axhline(P_ATM)
plt.axvline(oneATMTemp)

plt.yscale("log")

plt.legend(["Water 1-99°C", "Water 99-374°C", "Barometric pressure (760 mmHg)", "Vapour Temperature at 1 Bar"])

plt.xticks([0, 50, oneATMTemp, 150, 200, 250, 300, 350])

plt.xlabel("Temperature / °C")
plt.gca().xaxis.set_major_formatter(FormatStrFormatter("%.3f"))
plt.ylabel("Pressure / mmHg")

output_path = Path(__file__).with_name("vapour_pressure_python.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()
