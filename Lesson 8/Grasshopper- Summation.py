def summation(num):
    sum=0
    if num==0:
        return sum
    else:
        sum+=(num+summation(num-1))
    return sum

# def summation(num):
#     return sum(range(1,num+1))
    