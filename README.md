# Number Prettifier

## Language: Python3

Write tested code that accepts a numeric type and returns a truncated, "prettified" string version.
The prettified version should include one number after the decimal when the truncated number is not an integer.
It should prettify numbers greater than 6 digits and support millions, billions and trillions.

**Examples**:
```
   input: 1000000
   output: 1M

   input: 2500000.34
   output: 2.5M

   input: 532
   output: 532

   input: 1123456789
   output: 1.1B

   input: 9487634567534
   output: 9.5T
```

## Logic Explained

The main logic here for determining the appropriate suffix to apply is as follows: 
Divide by 1000 on each loop and stop when the final number is less than 1000. This will give you the count of the magnitude which will dictate which suffix you use, for example, ‘M’ or ‘B’.

And it happens on this line inside the `while` loop:

```
num = round(num / 1000.0, round_to)
```

## Run Instructions

In your terminal:

* Use this command to run the **code**:
`python number_prettifier.py`

* Use this command to to run the **unit tests**:
`python test_number_prettifier.py`

After running the code you will be prompted to enter a numerical value.