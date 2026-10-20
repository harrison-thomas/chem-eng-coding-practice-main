# 02: Mass Balance Solver

**Status:** In Progress
**Tools:** Python / MATLAB / Excel  
**Time spent:** ~3 hours

---

## Problem

This project solves steady-state mass balances for a small process flowsheet by writing the component and total balances as a linear system (Ax = b) and solving for all unknown stream flows and compositions at once. Results are cross-checked between Python and Excel, and the solver checks that the balances close and flags under- or over-specified problems using a degrees-of-freedom analysis.

## Expected result (written BEFORE coding)

Mass Balance should be consistent with my own solved answer and have the same values across both the python and excel methods of solving.

Hand solved result:  
Stream 3 total flow rate = 150kg/h
Stream 3 composition = 1/3 ethanol, 2/3 water
Stream 4 flow rate = initially 56.6825kg/h, but corrected to 56.667kg/h
Stream 5 flow rate = 93.33kh/h

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
- [X] Total mass balance for each unit
- [X] Component balance for each component in each unit
- [X] Any extra relationships (split fractions, specified recoveries)
- [X] Note which balances are redundant (e.g. component balances plus composition constraints can duplicate the total balance)

**4. Convert to matrix form (Ax = b)**
- [X] Decide the order of the unknowns in `x`
- [X] Decide what each row of `A` represents and what each column represents
- [X] Put all known values into `b`
- [X] Check dimensions: is `A` square?

**5. Solve it in two tools**
- [X] Python: solve the linear system with NumPy
- [X] Excel: solve it with matrix functions (or Solver as a cross-check)
- [X] Compare both against your hand solution

**6. Validate**
- [X] Do all balances close (in = out) to within rounding?
- [X] Are all flows positive and all mass fractions between 0 and 1?
- [X] Do the fractions in each stream sum to 1?

**8. Extend (optional)**
- [ ] Automate building `A` and `b` from a description of the streams and units
- [ ] Add a recycle stream and see what changes

## Results

Python:  

Solving the mass balances as a linear system `A x = b` gives:

| Stream | Quantity | Value | Units |
|--------|----------|-------|-------|
| F3 | Total flow (from F1 + F2) | 150 | kg/h |
| F3 | Ethanol mass fraction | 0.3333 | kg/kg |
| F4 | Total flow | 56.667 | kg/h |
| F5 | Total flow | 93.333 | kg/h |

**System solved** (unknowns `x = [x_3_ethanol, F4, F5]`):

```
┌                    ┐ ┌          ┐   ┌     ┐
│  150    0      0   │ │ x_3_eth  │   │  50 │
│    0    1      1   │ │   F4     │ = │ 150 │
│ -150   0.8   0.05  │ │   F5     │   │   0 │
└                    ┘ └          ┘   └     ┘
```

Row 1 is the ethanol balance on the mixer, row 2 the total balance on the separator, and row 3 the ethanol balance on the separator.

**Agreement with hand calculation:** Python and hand-solved values agree to [number of decimal places / `np.allclose` result].

**Residual** `A @ x - b`: [max absolute value]

## Validation

How did you check the result is right?

- Compared with: Hand calculated values 
- Sanity checks: Mass balance closes, and (A @ x - b) is reasonably close to 0
- Excel solver provides consistent answers

## What I learned

- Difference between np.array and np.matrix, as only by using an array could I index within the sublists
- A clean solve doesnt mean correct answers: I had to correct some values in A and b to get the correct answer even though the matrix was successfully being solved
- Matrix multiplication in excel - using MMULT and MINVERSE

## Limitations and next steps

- Just 2 components, hard coded numbers, fixed flowsheet
- Still need to automate the filling of A and b

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
