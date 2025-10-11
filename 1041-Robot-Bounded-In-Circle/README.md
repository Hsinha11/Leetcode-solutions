# Robot Bounded in Circle

## Problem Statement

You are given a string `instructions` consisting of characters `'G'`, `'L'`, and `'R'`, which represent:

- `'G'`: Move forward by 1 unit in the current direction.
- `'L'`: Turn left by 90 degrees.
- `'R'`: Turn right by 90 degrees.

A robot starts at the origin `(0, 0)` facing **north** (upwards along the y-axis). The robot repeats the instructions infinitely. Your task is to determine if the robot is **bounded in a circle**.  

Return `True` if there exists a circle such that the robot never leaves it, otherwise return `False`.

> **Note:** We are checking if the robot **never leaves some circle**. We do not simulate infinite steps; instead, we analyze the robot's position and direction after **one cycle of instructions**.

---

## Solution Logic

We can solve this problem by simulating the movement of the robot **once** and analyzing its final position and direction:

1. **Represent direction as a vector** `(dirX, dirY)`:
   - Initially facing north: `(0, 1)`.
   - East: `(1, 0)`, South: `(0, -1)`, West: `(-1, 0)`.

2. **Simulate the instructions**:
   - `'G'`: Move forward → `(x, y) = (x + dirX, y + dirY)`.
   - `'L'`: Turn left → `(dirX, dirY) = (-dirY, dirX)` (rotate 90° counterclockwise).
   - `'R'`: Turn right → `(dirX, dirY) = (dirY, -dirX)` (rotate 90° clockwise).

3. **Check if robot is bounded**:
   - If robot returns to origin `(0,0)`, it is bounded.
   - If robot does **not face north** after executing the instructions once, it will eventually loop in a circle.

---

## Python Implementation

```python
class Solution(object):
    def isRobotBounded(self, instructions):
        # Initial direction: facing north
        dirX, dirY = 0, 1
        # Initial position at origin
        x, y = 0, 0

        # Process each instruction
        for d in instructions:
            if d == "G":
                x, y = x + dirX, y + dirY
            elif d == "L":
                dirX, dirY = -dirY, dirX  # Turn left 90 degrees
            else:
                dirX, dirY = dirY, -dirX  # Turn right 90 degrees

        # Robot is bounded if it returns to origin
        # or doesn't face north after one cycle
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)
```

---

## Time and Space Complexity

### Time Complexity: **O(n)**
- **Where n is the length of the `instructions` string**
- We iterate through each character in the instructions exactly **once**
- Each operation (`'G'`, `'L'`, `'R'`) takes **constant time O(1)**:
  - `'G'`: Simple arithmetic operations (addition)
  - `'L'` and `'R'`: Simple variable assignments
- **Total operations**: n iterations × O(1) per iteration = **O(n)**

### Space Complexity: **O(1)**
- **Constant extra space** regardless of input size
- We only use a **fixed number of variables**:
  - `dirX`, `dirY` (direction vector)
  - `x`, `y` (position coordinates)
- **No additional data structures** like arrays, hash maps, or recursion stack
- **Space usage is independent** of the input size n

### Why This Approach is Optimal
1. **We only simulate once**: Instead of simulating infinite repetitions, we analyze the pattern after one cycle
2. **Mathematical insight**: If the robot doesn't return to origin and faces north, it will move away indefinitely. If it faces any other direction, it will trace a bounded path
3. **No need for complex data structures**: Simple arithmetic operations are sufficient

### Example Analysis
- **Input**: `"GGLLGG"` (length = 6)
- **Time**: 6 iterations × O(1) = **O(6) = O(n)**
- **Space**: 4 variables = **O(1)**
