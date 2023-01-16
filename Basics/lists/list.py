# Program to print second largest of given numbers

#create an empty list
numbers=[]

n=int(input("Length of the list : "))  #taking the length of list as input from user

for i in range(1,n+1): #looping means to execute a block of code in repeated manner, In this case the loop will iterate n times as the given range id from 1->n
    num=int(input("Enter number " + str(i) + ": ")) #Taking numbers as input from user and typecasting "i" which is an intger to string, as we can't concatenate string and integer
    numbers.append(num) #appending the numbers to the list

numbers.sort() #sorting the list in ascending manner using sort() method
sorted_list=(sorted(numbers)) #Sorted list

# print(sorted_list)
print( "The second largest number is : " + str(sorted_list[-2])) #accessing the second element from last using negative index