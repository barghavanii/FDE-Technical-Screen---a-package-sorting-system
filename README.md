# Package Sorting System

My solution for the Thoughtful FDE Technical Screen - a package sorting system for robotic automation.

## What It Does

This program sorts packages into different stacks based on their size and weight. It's designed to help robotic arms figure out which packages they can handle automatically and which ones need special treatment.

## The Rules

A package can be classified as:

**Bulky** if:
- Volume (Width × Height × Length) is 1,000,000 cm³ or more
- OR any dimension is 150 cm or greater

**Heavy** if:
- Mass is 20 kg or more

Based on these classifications, packages go into three stacks:
- **STANDARD** - Normal packages that aren't bulky or heavy
- **SPECIAL** - Packages that are either bulky or heavy (but not both)
- **REJECTED** - Packages that are both bulky and heavy

## Running the Code

Make sure you have Python 3.6+ installed. That's all you need - no external libraries required.

```bash
python exam_healthcare.py
```

You should see:
```
All tests passed! ✅

Example outputs:
sort(50, 50, 50, 10) = STANDARD
sort(150, 50, 50, 10) = SPECIAL
sort(50, 50, 50, 20) = SPECIAL
sort(150, 50, 50, 20) = REJECTED
```

## How to Use It

The main function is pretty straightforward:

```python
def sort(width, height, length, mass):
    """
    Args:
        width, height, length: in centimeters
        mass: in kilograms
    
    Returns:
        "STANDARD", "SPECIAL", or "REJECTED"
    """
```

Some examples:

```python
# Normal package
sort(50, 50, 50, 10)  # "STANDARD"

# One dimension is too big
sort(150, 50, 50, 10)  # "SPECIAL"

# Too heavy
sort(50, 50, 50, 20)  # "SPECIAL"

# Both bulky and heavy - rejected
sort(150, 50, 50, 20)  # "REJECTED"

# Volume calculation matters too
sort(100, 100, 100, 5)  # "SPECIAL" because volume = 1,000,000 cm³
```

## Testing

I included a bunch of tests to make sure everything works correctly, including edge cases like:
- Packages right at the threshold values
- Floating point precision issues
- Zero dimensions
- Really large packages

All tests are in the `test_sort()` function and run automatically when you execute the script.

## Implementation Notes

- Used ternary operators in the code (as specified in the requirements)
- The logic checks volume and dimension thresholds for bulkiness
- Then checks mass for heaviness
- Finally determines the stack based on both conditions


## About

This was written for Thoughtful's technical screening process. The challenge was to implement clean, working code with proper test coverage in under 30 minutes.
