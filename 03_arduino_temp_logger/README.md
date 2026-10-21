# 03: Arduino Temperature Logger

**Status:** In Progress
**Tools:** Python / Excel / Arduino / Plotting
**Time spent:** ~X hours

---

## Problem

Connect a temperature logger via an Arduino Breadboard to send regular inputs to python, which will display them on a live plot (temperature against time). Will also send the inputs to an Excel file, and can experiment with varying the time between inputs and % error in different environments.

## Expected result (written BEFORE coding)

Resultant plot should indicate any temperature changes (eg covering temperature logger with hand to increase), and ideally the plot should move with time (so can show over a longer time). Excel sheet should show the recorded termpature, and either the time taken or time since logging started.

## Theory

- Temperature Module: DHT11

Has an 8 bit microcontroller for processing sensor data and outputtinv digitally, removing need for an external analogue-to-digital converter.

Temperature range: 0-50°C, 2 degree accuracy. Operating voltage is 3-5V DC.

Sampling rate: 1Hz. Most have a built in resistor, but if not a 5-10KOhm resistor is needed.

- Software: Arduino, transmit sensor inputs to python for plotting

## Method

1. Research into the temperature module I have and what is required/syntax
2. Look into sending data between Arduino and python
3. Connect circuit via breadboard
4. Write the code in Arduino IDE
5. Test and amend as nessessary
6. Write the python script (plotting using Matplotlib)
7. Connect python and Arduinio
8. Test it (and break it)

## Results

![Description of the plot](plot.png)

Key numbers, with units. Add a table if you have several.

## Validation

How did you check the result is right?

- Compared with: (textbook value, hand calculation, NIST data, second tool)
- Difference: absolute and % (say which units, e.g. K vs °C)
- Sanity checks: (mass balances close, values physical, limits behave sensibly)

## Error analysis

- What are the plausible sources of error?
- Which did you **test** (e.g. changed step size, swapped coefficients), and what did you find?
- Which are still just hypotheses?

## What I learned

- Something technical
- Something about the tool or code
- One thing that surprised me

## Limitations and next steps

- What this model ignores
- How you could extend it (stretch ideas)

---

## Running the code

```
cd NN_title
python script_name.py
```

Requirements: list libraries (or point to `requirements.txt`).

## Files

| File          | Description                |
| ------------- | -------------------------- |
| `script.py` | Python version             |
| `script.m`  | MATLAB version             |
| `data.xlsx` | Excel version / input data |
| `plot.png`  | Output figure              |

## Sources

- Author, title, URL (accessed date)
- Cite the original source (e.g. NIST, a textbook), not just where you found it
