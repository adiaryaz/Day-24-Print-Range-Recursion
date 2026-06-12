# Day-24-Print-Range-Recursion
Day 24/100 - Python Program to Print Numbers in a Range Using Recursion

# Print Numbers in a Range (Recursive)
A program to display a sequence of numbers between a user-defined start and end value utilizing a recursive function.

## 📝 Description

This program takes a starting value (`start`) and an ending value (`end`) from the user. Instead of using traditional iteration tools like a `for` or `while` loop, it relies entirely on **recursion** to output the sequence.

The function continuously calls itself, incrementing the starting number by 1 during each call, and prints the current number. This process repeats until the starting number exceeds the ending number, which triggers the base case and strictly stops the recursion stack.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** An integer representing the starting value of the range (`start`).
* **Input 2:** An integer representing the ending value of the range (`end`).

### Output:

* The sequence of integers from `start` to `end`, with each number printed on a new line.

### Rules:

1. The program must accept two integer inputs from the user (`start` and `end`).
2. The program must use a **recursive function** (`print_range`) to handle the iteration.
3. **Base Case:** If `start > end`, the function must execute a `return` statement to terminate the recursion.
4. **Recursive Step:** The function must print the current `start` value and then call itself with `start + 1`.

---

## 💡 Examples

### Example 1

**Input:**

```
1
5


```

**Output:**

```
1
2
3
4
5


```

**Explanation:** The function prints 1, then recursively calls itself with 2. This continues until it prints 5. When it calls itself with 6, the condition `6 > 5` is met, and the recursion stops.

### Example 2

**Input:**

```
10
12


```

**Output:**

```
10
11
12


```

**Explanation:** The program outputs the numbers 10, 11, and 12 on separate lines sequentially before naturally terminating.

### Example 3 (Single Number Range)

**Input:**

```
7
7


```

**Output:**

```
7


```

**Explanation:** The starting and ending numbers are exactly the same. It prints 7, increments to 8, and immediately hits the base case (`8 > 7`), stopping the function.

### Example 4 (Invalid Range)

**Input:**

```
5
1


```

**Output:**

```



```

**Explanation:** Because the initial starting number (5) is already greater than the ending number (1), the base case condition (`5 > 1`) is met on the very first function call, resulting in no output.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-24-Print-Range-Recursion.git
cd print-range-recursion


```

2. **Run the program**:

```bash
python main.py


```

Enter the starting and ending numbers when prompted to see the resulting sequence printed to the console.
