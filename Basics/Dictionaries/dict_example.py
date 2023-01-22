#Program to calculate the rank of the students

data = {} #Creating an empty dictionary

n = int(input("Enter no. of Students : "))

for i in range(n):
    name=input(f'\nStudent {i+1} : ') #input keys (names of the students)
    marks=int(input(f"{name}'s total marks : ")) #input values (marks of the student)
    data[f"{name}"]=marks #updating the dictionary


sorted_dict=dict(sorted(data.items(),reverse=True,key=lambda item:item[1])) #Sorting the dictionary by marks(i.e, by Values),"key" parameter is passed to perform a custom sort that's why index 1 is used in lambda function for values as index 0 is reserved for keys. 
sorted_list=list(sorted_dict.keys())


print(f"\nCongratulations!! {sorted_list[0]} for being the 1st rank holder.\n")

print("Other's rank are as follow : \t")

for i in range(len(sorted_list)):
    print(f"\tRank {i+1} : {sorted_list[i]}") #printing the list w.r.t their index value