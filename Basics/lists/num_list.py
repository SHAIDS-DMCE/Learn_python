odd_list=[1,3,5,7,9]
even_list=[2,4,6,8,10]

combined_list=(odd_list + even_list)
print(combined_list)

for i in range(3):
    num=int(input(f"Enter numbers {i+1} : ")) #inserting 3 numbers
    combined_list.insert(i,num)

print(combined_list)
print(f"Length of the list is {len(combined_list)}")

combined_list[-1]=100
combined_list[-2]=200
combined_list[-3]=300
print(combined_list)

combined_list.clear()
print(combined_list)
