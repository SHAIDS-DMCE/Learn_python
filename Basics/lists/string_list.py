list1=['Anil','Amol','Aditya','Avi','Alka']

list1.insert(2,"Anuj")
print(list1) #Insert

list1.append("Zulu") #append
print(list1)

list1.remove("Avi") #delete Avi
print(list1)

list1[0]="Anilkumar" #Replace
print(list1)

list1.sort()
print(sorted(list1)) #Sorted list

list1.sort()
print(sorted(list1,reverse=True)) #reverse Sorted list
