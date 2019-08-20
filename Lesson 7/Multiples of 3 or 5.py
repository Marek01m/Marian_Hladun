def solution(number):
    num_list=[x for x in range(number) if x%3==0 or x%5==0]
    return sum(num_list)
    