#TAsk1

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names) 


# names = ['Sam', 'Don', 'Daniel'] 
# print(list(map(lambda n:hash(n),names)))

#print(list(map(hash,names)))



##########################################################
#task 2

# color_list = [“red”, “green”, “black”, “red”, “brown”, “red”, “blue”, “red”, “red”, “yellow” ]

# sort_red=list(filter(lambda x: x=="red",color_list))
# print(sort_red)


################################################
#task 3

# my_list=["1","2","3","4","5","6","7"]

#_______apend method
# new_list=[]

# for i in my_list:
#     new_list.append(int(i))

# print(new_list)    

#_____________________map method

# result=list(map(lambda x: int(x), my_list))
# print(result)


###########################################
#Task 4

# def miles_to_kilometers(num_miles):
#     return round(num_miles * 1.6,2)
# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(miles_to_kilometers, mile_distances))
# print (kilometer_distances)


##############
# my_list=list(range(2,10,2))
# print(my_list)

# print(list(map(lambda x: round(x*1.6) ,my_list)))