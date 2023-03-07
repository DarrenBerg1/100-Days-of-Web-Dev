[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10091491&assignment_repo_type=AssignmentRepo)
# Assessment 1: Algorithms
- **Change Maker**


## Important Grading Information
- Make sure you read the [Assessment-1 Grading Rubric](https://docs.google.com/spreadsheets/d/1CjVoEPvswccsGTU5xc0WLaQ87Ql_mqGSeCEoZhSFyCM/edit?usp=sharing).
  - Algorithm Correctness (60%)
  - Code Design (40%)
- You need to get a 75% or better to pass. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment... 
  - *5% penalty*: If you complete and submit the retake **within one week** of receiving your grade. 
  - *10% penalty*: If you complete and submit the retake **by 8:30am, May 15th, 2023**. A retake for this assessment WILL NOT be accepted after this date.
  
## Rules / Process
- This assignment is fully open notes and open Google, but is not to be completed with the help of any other student/individual.

## Requirements
- This assessment should be completed using Python.

## Challenge
You are writing a program for an electronic vending machine to give you the optimal change for an item's cost. Write a function called `optimal_change` that takes in two arguments: `item_cost` and `amount_paid`. The function should return a string describing the optimal change which follows the following convention:

```py
print(optimal_change(62.13, 100))
> "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

print(optimal_change(31.51, 50))
> "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
```

Some helpful notes:
- Your algorithm should compute the **optimal** change. Obviously, you can give the change in pennies, but we're looking for the most optimal (least amount of) change possible.
- You should only consider *common* monetary denominations (i.e. ignore any denomination larger than $100-bill, ignore $2-bills, half-dollars, etc...)
- Valid denominations: 1 cent (penny), 5 cents (nickel), 10 cents (dime), 25 cents (quarter), $1, $5, $10, $20, $50, $100
- $1 = 100 cents  ==> 1 penny = $0.01 , 1 nickle = $0.05, 1 dime = $0.10, 1 quarter = $0.25
- You should fully understand the data types of your input and output
- You need to account for proper plural denominations (i.e., quarters, dimes, pennies, bills) and proper punctuation (i.e., commas, using "and", and the period at the end of a sentence).
- Hint: If you run into issues with having too many digits after decimal point look into rounding your number to 2 decimal places

The correctness portion of this assignment will be autograded using the `autograde_test.py` file. PLEASE DO NOT MODIFY THIS FILE!
To run it locally, use the command
```sh
pytest autograde_test.py
```
When you push your code back up to your repo the tests should run automatically and give you a score.


Testing is important for any application that is written. We have provided you with an empty spec file to use to test your code.

Sample test cases:
```py

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

```
BONUS POINT: Your tests should be checking for special cases that might cause your program to break. Provide tests for those cases in the spec file. We haven't specified what to return for these special cases so choose what you think is most sensible. 
