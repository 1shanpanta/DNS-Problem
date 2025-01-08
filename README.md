# Developer Internship Task Solution – I

## Task Overview

The challenge was to create a formula using the digits **1, 2, 3, 4, and 5**—each used **exactly once**—to equal **2025**, while adhering to the rules:

- Use each number only once.
- Apply standard mathematical operations (addition, subtraction, multiplication, division, exponentiation, etc.).
- Parentheses were allowed to define the order of operations.

---

## My Thought Process

While working on this problem, I couldn’t help but notice how **special** the number 2025 is:

- It is made up of two **perfect squares**, \(25 = 5^2\) and \(81 = 3^4\).
- The number 2025 itself is a **perfect square**, as \(2025 = 45^2\).
- It is rare to encounter such numbers in mathematics where both the factors and the number itself exhibit such symmetry and elegance.

With this insight, I decided to break down 2025 into its components (\(25\) and \(81\)) and further factored these until I was left with the digits **1, 2, 3, 4, and 5**. My goal was to find a way to represent 2025 using these digits while adhering to the rules of the challenge and capturing the **beauty of the number**.

---

## My Solution

After factoring and exploring different combinations, I arrived at this formula:

```

3^(4 * (2 - 1)) * 5^2 = 2025 ( 81 * 25)


```

### Verification

Here’s the step-by-step breakdown of the formula:

1. **Simplify the parentheses**:\[
   (2 - 1) = 1
   \]
2. **Solve the exponents**:\[
   4 * (2 - 1) = 4 * 1 = 4
   \]\[
   3^4 = 81
   \]\[
   5^2 = 25
   \]
3. **Multiply the results**:
   \[
   81 times 25 = 2025
   \]

---

## Reflections on the Solution

While finding this formula, I aimed to make the representation not only correct but also **beautiful** in its structure. In doing so, I was inspired by both the mathematical elegance of 2025 and the following philosophies:

### 1. **The Beauty of Symmetry**

Breaking 2025 into its square factors (\(81 = 3^4\) and \(25 = 5^2\)) felt like uncovering a **hidden symmetry** within the number. Both components are perfect squares, and their combination forms another perfect square, \(45^2\). The formula celebrates this symmetry.Maybe this year 2025 might turn out to be perfect as well!

### 2. **Wabi-Sabi (侘寂 – Imperfect Perfection)**

In Japanese philosophy, **Wabi-Sabi** teaches us to find beauty in simplicity and imperfection. While the formula itself may appear simple, the process of finding it—through trial, error, and reflection—was far from perfect. This journey mirrors the philosophy of finding beauty in the imperfect.

---

## Python Code for Validation

To validate the formula, I wrote a simple Python script:

```python
from math import pow
def verify_2025():
    # Using the formula: 3^(4 * (2 - 1)) * 5^2
   
    result = pow(3, 4 * (2 - 1)) * pow(5, 2)
    return result

if __name__ == "__main__":
    print("The result is:", verify_2025())  # Should print 2025.0
```
