# 💻 Command Line Interface (CLI) Calculator

A robust, interactive command-line calculator written in pure Python.

---

## 🛠️ Features

- **Standard Arithmetic**: Support for addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- **Input Validation**: Safe handling of division-by-zero errors.
- **Interactive Session**: Continuous processing loop so you can perform multiple calculations in one run.
- **Quick Exit**: Type `!` as the operation to close the application immediately.

---

## 🚀 How to Run

No external dependencies are required to run the CLI calculator. 

```bash
python calculator.py
```

---

## 📖 Step-by-Step Usage

1. **Start the program**: Run the command above in your terminal.
2. **Select an Operator**:
   - `+` : Addition
   - `-` : Subtraction
   - `*` : Multiplication
   - `/` : Division
   - `!` : Exit program
3. **Provide Inputs**: Enter your first and second numbers when prompted.
4. **View Result**: The program calculates the value, prints it, and prompts you for the next operation.

### Example Interaction

```text
Enter operation (+, -, *, /,!): +
Enter first number: 12
Enter second number: 8
Result: 20

Enter operation (+, -, *, /,!): /
Enter first number: 10
Enter second number: 0
Error: Division by zero

Enter operation (+, -, *, /,!): !
Calculator Closed
```

---

## 🔍 Code Overview

The calculator uses a `while True` loop to keep running until it encounters the `!` exit condition. It processes operations using standard conditionals and validates the denominator before executing division.

```python
# Code snippet of the core logic:
if operator == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print("Result:", num1 / num2)
```
