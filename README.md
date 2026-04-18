# 🧮 CLI Calculator using Reverse Polish Notation (RPN)

A simple command-line calculator built in Python that evaluates mathematical expressions using the **Shunting Yard Algorithm** and **Reverse Polish Notation (RPN)**.

---

## 🚀 Features

* Supports basic arithmetic operations:

  * Addition `+`
  * Subtraction `-`
  * Multiplication `*`
  * Division `/`
* Handles:

  * Multi-digit numbers
  * Decimal values (e.g., `12.5`)
  * Parentheses for precedence `( )`
* Converts infix expressions → RPN → evaluates result
* Basic error handling:

  * Invalid expressions
  * Division by zero

---

## 🧠 How It Works

The calculator processes expressions in **three stages**:

### 1. Tokenization

Converts input string into tokens:

```text
"2+3*4" → [2.0, '+', 3.0, '*', 4.0]
```

---

### 2. Infix → RPN Conversion

Uses the **Shunting Yard Algorithm** to handle operator precedence:

```text
[2.0, '+', 3.0, '*', 4.0]
→
[(Operand, 2.0), (Operand, 3.0), (Operand, 4.0), (Operator, '*'), (Operator, '+')]
```

---

### 3. Evaluation

Processes RPN using a stack:

```text
2 3 4 * + → 14
```

---

## 📦 Project Structure

```text
calc.py
```

### Key Functions:

* `tokeniser(expression)`
  Converts input string into tokens

* `convert_to_rpn(tokens)`
  Converts tokens into Reverse Polish Notation

* `evaluator(output)`
  Evaluates the RPN expression

* `solve(a, b, operator)`
  Performs arithmetic operations

---

## ▶️ Usage

Run from terminal:

```bash
python calc.py "2+3*4"
```

### Example Outputs

```bash
$ python calc.py "2+3"
5.0

$ python calc.py "2+3*4"
14.0

$ python calc.py "(2+3)*4"
20.0

$ python calc.py "2+3+4+5*3/3"
14.0
```

---

## ⚠️ Limitations (Current Scope)

This version supports **valid expressions only**. The following are NOT handled yet:

* Negative numbers (e.g., `-3 + 2`)
* Implicit multiplication (e.g., `2(3+4)`)
* Multiple operators (e.g., `2++3`)
* Exponentiation (`^`)

---

## 🔮 Future Improvements

* Support negative numbers
* Add exponentiation operator
* Better input validation
* Improve tokenizer (handle implicit multiplication)
* Add unit tests
* Convert into a reusable Python module

---

## 🛠️ Concepts Used

* Stack data structure
* Expression parsing
* Shunting Yard Algorithm
* Reverse Polish Notation (RPN)
* Function design & modularization

---

## 🎯 Learning Outcome

This project demonstrates how to:

* Break down a problem into stages
* Build a simple interpreter-like system
* Handle operator precedence and parsing logic
* Write modular and maintainable Python code

---

## 💡 Author Notes

This project was built as part of a learning process to strengthen:

* Problem-solving skills
* Understanding of parsing algorithms
* Writing structured Python code

---

## 📌 Run Tips

* Always wrap expressions in quotes:

  ```bash
  python calc.py "3+4*2"
  ```
* Avoid spaces unless handled explicitly

---

## 🏁 Final Thoughts

This is a foundational project that mimics how real expression evaluators work under the hood. It’s a great step toward building more complex systems like interpreters or compilers.

---


Summary:
# 🧮 CLI Calculator (RPN based)

A simple Python CLI calculator that evaluates expressions using the **Shunting Yard Algorithm** and **Reverse Polish Notation (RPN)**.

---

## 🚀 Features

* Supports: `+  -  *  /`
* Handles:

  * Multi-digit & decimal numbers
  * Parentheses `( )`
* Basic error handling (invalid expressions, divide by zero)

---

## 🧠 How it works

1. **Tokenize** → `"2+3*4"` → `[2.0, '+', 3.0, '*', 4.0]`
2. **Convert to RPN** → `2 3 4 * +`
3. **Evaluate** → `14`

---

## ▶️ Usage

```bash
python calc.py "2+3*4"
```

### Examples

```bash
"2+3"        → 5.0
"2+3*4"      → 14.0
"(2+3)*4"    → 20.0
```

---

## ⚠️ Limitations

* No negative numbers (`-3 + 2`)
* No implicit multiplication (`2(3+4)`)
* No exponentiation (`^`)

---

## 🛠️ Key Functions

* `tokeniser()` → creates tokens
* `convert_to_rpn()` → handles precedence
* `evaluator()` → computes result

---

## 🎯 Goal

Understand parsing, stacks, and how expression evaluators work.

---



