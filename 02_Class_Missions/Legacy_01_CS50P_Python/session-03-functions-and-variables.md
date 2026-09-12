# Legacy Gap-Fill Mission — Functions, Variables, and Input/Output

**Use only when Session 3 diagnostic evidence shows a Python gap.**  
**Typical duration:** 45–75 minutes depending on need  
**No required pre-class viewing.**

This packet is retained inside the legacy `02_Class_Missions/Legacy_01_CS50P_Python/` folder for compatibility. It is **not** part of a mandatory CS50P sequence.

## Learning Cycle

```text
Learn → Practice → Rebuild → Share
```

The exact timing can change. Students who recover the target skill quickly should move forward rather than complete redundant work.

## Learning Target

By the end of this mission, you can explain and use Python values, variables, input/output, functions, parameters, and return values in a short program.

## Resource Choice

Use the shortest resource that addresses the diagnosed gap.

Preferred options:

1. **CodeHS Data Science with Python — Basic Python Bootcamp** for targeted practice;
2. teacher mini-lesson and examples in this packet;
3. **CS50P** only as optional reference or extension.

Do not assign a full CS50P lecture as required preparation for this mission.

## 1. Learn — Core Pattern

```text
input value → variable → processing expression/function → return value → output
```

Key distinctions:

- `print(...)` displays a value;
- assignment stores a value in a variable;
- a parameter receives a value when a function is called;
- `return` sends a value back to the caller.

Example:

```python
def double(number):
    return number * 2

value = int(input("Number: "))
result = double(value)
print(result)
```

Trace it as:

```text
Input value:
Stored variable:
Function called:
Parameter value:
Returned value:
Printed output:
```

## 2. Practice

### Trace A

Predict the final output and explain each stored value.

```python
def add_tax(price):
    return price * 1.1

cost = 20
final_cost = add_tax(cost)
print(final_cost)
```

### Trace B

Explain why these two functions behave differently:

```python
def show_square(x):
    print(x * x)


def get_square(x):
    return x * x
```

### Short Build

Write a function that:

1. receives one number as a parameter;
2. performs one calculation;
3. returns the result;
4. stores the returned value;
5. prints the stored result outside the function.

## 3. Rebuild

Without copying a complete solution, rebuild a small input → process → output program.

Requirements:

- at least one user input;
- at least one variable;
- one function with a parameter;
- one returned value;
- output produced outside the function.

Documentation, hints, and debugging support may be used according to the club AI-use policy, but the student must be able to explain every line submitted.

## 4. Share / Evidence

Submit:

- one completed program trace;
- the independent rebuild;
- one error encountered and how it was corrected;
- a short explanation of `print` versus `return`;
- a meaningful Git commit;
- `ai_usage_note.md` when applicable.

## Exit Check

A student is ready to leave this gap-fill mission when they can answer all four without notes:

1. What value is stored in a variable after an assignment?
2. What is passed into a parameter?
3. What does `return` do?
4. Why can a returned value be reused while printed output alone usually cannot?

Once the student meets the target, return to the current IOAI/Year A pathway rather than continuing through legacy Python packets automatically.