# Dictionaries
Dictionary is an unordered collection of key-value pairs. Each entry has a key and value. A dictionary can be considered as a list with special index.

The keys must be unique and immutable. So we can use strings, numbers (int or float), or tuples as keys. Values can be of any type.

Consider a case where we need to store phone numbers. We can either store them in a dictionary or a list.

## List

|Index | Numbers|          
|:------:|-----------|
|0|9920297854|
|1|7450297854|
|2|9925897854|
|3|9478297854|

## Dictionary

|Keys | Values|          
|:------:|-----------|
|Yuno|9920297854|
|Asta|7450297854|
|Yami|9925897854|
|Noelle|9478297854|

Example
```python
magic_squad = {
    "Squad":"Black Bulls",
    "Captain":"Yami Sukehiro", #Creating a Dictionary
    "rookie":"Asta"
}

print(magic_squad) #printing dictionary
print(magic_squad["Captain"]) #Printing the value of a key in dictionary
```
```
{'Squad': 'Black Bulls', 'Captain': 'Yami Sukehiro', 'rookie': 'Asta'}

Yami Sukehiro
```

 [Methods in Dictionary](https://www.w3schools.com/python/python_dictionaries_methods.asp)

## Other useful links
[W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)

[Exercise](https://www.geeksforgeeks.org/python-dictionary-exercise/)