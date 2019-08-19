def count_positives_sum_negatives(arr):
    pos=[i for i in arr if i>0]
    neg=[i for i in arr if i<0]
    return [len(pos),sum(neg)] if arr else []
    
