# Conditional Statements
Conditional statements are usually wrritten in if....else.... blocks, where if the condition returns a true value then the "if block" will execute, else "else block" will be executed.

## If...Else...
```python
a = 10
b = 25

if b > a:
    print("b is greater than a")

else:
    print("a is greater than b")
```
Output :
```
b is greater than a
```
## elif...
In case, User have more than one condition, "elif" (Else If) blocks are used

Example :
```python
age = int(input("Enter your age : ")) #Takes user's age as input.

if age >= 18 :
    print("You are eligible to vote")

elif 0 > age < 18 :
    print("Try again, after you are 18+")

else :
    print("Enter a valid age") #for negative inputs
```
Output : <br>
for age = 20 :
```
You are eligible to vote
```
for age = 15 :
```
Try again, after you are 18+
```
for age = -16
```
Enter a valid age
```
## Mostly used operators
|Operator|Operation|Example|
|:---:|:---:|:---:|
|+|Addition|x + y|
|-|Subtraction|x - y|
|*|Multiplication|x * y|
|/|Division|x / y|
|//|Floor Division|x // y|
|**|Exponentiation|x ** y|
|%|Modulus|x % y|
|==|Equal|x == 5|
|!=|Not equal|x != y|
|>|Greater than|x > y|
|<|Lesser than|x < y|
|>=|Greater than or equal to|x >= y|
|<=|Less than or equal to|x <= y|
|and|Returns True if both statements are true|x = y and x = 5|
|or|Returns True if one of the statements is true|x = y or x = 5|
|not|Reverse the result, returns False if the result is true|not(x = y and x = 5)|

## Other Useful links
- [Real Python](https://realpython.com/python-conditional-statements/)
- [W3Schools](https://www.w3schools.com/python/python_conditions.asp)
- [Codes Dope (Exercise)](https://www.codesdope.com/practice/python-decide-ifelse/)
- [Exercise](https://csiplearninghub.com/python-if-else-conditional-statement-practice/)
