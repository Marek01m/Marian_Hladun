# def count_sheeps(arrayOfSheeps):
#     count=0     
#     for i in arrayOfSheeps:
#         if i==True:
#             count+=1
#         else:
#             continue
#     return count       
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
