# 02: Mass Balance Solver

**Status:** In Progress
**Tools:** Python / MATLAB / Excel  
**Time spent:** ~X hours

---

## Problem

This project solves steady-state mass balances for a small process flowsheet by writing the component and total balances as a linear system (Ax = b) and solving for all unknown stream flows and compositions at once. Results are cross-checked between Python and Excel, and the solver checks that the balances close and flags under- or over-specified problems using a degrees-of-freedom analysis.

## Expected result (written BEFORE coding)

Mass Balance should be consistent with my own solved answer and have the same values across both the python and excel methods of solving.

## Theory

- Stream input = Stream output
- System here is steady state, so there is no changing process characteristics

- Degree of freedom analysis
    4 unknowns:
    F3 Composition
    F3 Flow rate
    F4 Flow rate
    F5 Flow rate

    4 independent equations:
    Ethanol in mixer = ethanol out mixer
    Water in mixer = water out mixer
    Ethanol in seperator = Ethanol out seperator
    Water in seperator = Water out seperator

    Degrees of freedom = 4 - 4 = 0 
    Therefore the system can be solved in principle

## Method

**1. Define the system**
- [X] Choose a small flowsheet (e.g. one mixer + one separator, 2 components) and sketch it
- [X] Label every stream (F1, F2, ...) and every unit (M1, S1, ...)
- [X] List what is known (flows, compositions, split fractions) and what is unknown
- [X] Solve it by hand first, so you have an answer to check against

**2. Degrees of freedom analysis**
- [X] Count unknowns and independent equations for each unit and for the whole system
- [X] Predict: is the problem solvable, under-specified or over-specified?
- [X] Record the prediction *before* running any code

**3. Write the balances**
- [ ] Total mass balance for each unit
- [ ] Component balance for each component in each unit
- [ ] Any extra relationships (split fractions, specified recoveries)
- [ ] Note which balances are redundant (e.g. component balances plus composition constraints can duplicate the total balance)

**4. Convert to matrix form (Ax = b)**
- [ ] Decide the order of the unknowns in `x`
- [ ] Decide what each row of `A` represents and what each column represents
- [ ] Put all known values into `b`
- [ ] Check dimensions: is `A` square? If not, why not?

**5. Solve it in two tools**
- [ ] Python: solve the linear system with NumPy
- [ ] Excel: solve it with matrix functions (or Solver as a cross-check)
- [ ] Compare both against your hand solution

**6. Validate**
- [ ] Do all balances close (in = out) to within rounding?
- [ ] Are all flows positive and all mass fractions between 0 and 1?
- [ ] Do the fractions in each stream sum to 1?

**7. Break it on purpose**
- [ ] Remove one specification (under-specified): what does each tool do?
- [ ] Add one redundant specification (over-specified, consistent): what happens?
- [ ] Add one contradictory specification: what happens?
- [ ] Compare these results with your degrees-of-freedom prediction from step 2

**8. Extend (optional)**
- [ ] Automate building `A` and `b` from a description of the streams and units
- [ ] Add a recycle stream and see what changes

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

| File | Description |
|------|-------------|
| `script.py` | Python version |
| `script.m` | MATLAB version |
| `data.xlsx` | Excel version / input data |
| `plot.png` | Output figure |

## Sources

- Author, title, URL (accessed date)
- Cite the original source (e.g. NIST, a textbook), not just where you found it
