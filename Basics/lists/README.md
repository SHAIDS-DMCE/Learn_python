
# Lists

Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.

Lists are always created using square brackets.

```python
ex_list = []   #Creating an empty list

ex_list.append(1)  #append the items to the list
ex_list.append(2)
ex_list.append(3)

print(ex_list)   #prints new list
```

output 
```
[1,2,3]
```
## Methods in list
| Method             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| [append()](https://www.w3schools.com/python/ref_list_append.asp) | Adds an element at the end of the list |
| [clear()](https://www.w3schools.com/python/ref_list_clear.asp) | Removes all the elements from the list|
| [copy()](https://www.w3schools.com/python/ref_list_copy.asp) | Returns a copy of the list|
| [count()](https://www.w3schools.com/python/ref_list_count.asp)| Returns the number of elements with the specified value |
|[extend()](https://www.w3schools.com/python/ref_list_extend.asp)|Add the elements of a list (or any iterable), to the end of the current list|
|[index()](https://www.w3schools.com/python/ref_list_extend.asp)|Returns the index of the first element with the specified value|
|[insert()](https://www.w3schools.com/python/ref_list_insert.asp)|Adds an element at the specified position|
|[pop()](https://www.w3schools.com/python/ref_list_pop.asp)|Removes the element at the specified position|
|[remove()](https://www.w3schools.com/python/ref_list_remove.asp)|Removes the item with the specified value|
|[reverse()](https://www.w3schools.com/python/ref_list_reverse.asp)|Reverses the order of the list|
|[sort()](https://www.w3schools.com/python/ref_list_sort.asp)|Sorts the list|

## List Comprehension
List comprehension is basically creating lists based on other iterables such as lists, tuples, sets, and so on. It can also be described as representing for and if loops with a simpler and more appealing syntax. List comprehensions are relatively faster than for loops.

Syntax : 
```python
list = [Expression for item in iterable (if conditional)]
```
For example :
```python
list1 = [1,2,3,4,5,6,7,8,9,10]

even_list=[x for x in list1 if x%2==0] #list of even numbers in list1
print(even_list)
```
```
[2,4,6,8,10]
```

## Other useful links
- [W3Schools](https://www.w3schools.com/python/python_lists.asp)
- [Geeks for geeks](https://www.geeksforgeeks.org/python-lists/)
- [Exercise](https://www.geeksforgeeks.org/python-list-exercise/)