my_list = [] #creating an empty list

my_list.append(10) #appending the elements to the list
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15) #inserting the value 15 at the second position in the list 

my_list.extend([50,60,70]) #extending the list with another list

my_list.remove(70) #removing the last element from the list

my_list.sort() #sorting the list in ascending order

print(my_list) #printing the list

print(my_list.index(30)) #finding the index of the value 30 in the list

