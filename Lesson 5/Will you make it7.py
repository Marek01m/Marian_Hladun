def zero_fuel(distance_to_pump, mpg, fuel_left):
    possible=None
    if distance_to_pump<=fuel_left*mpg:
        possible=True
    else:
        possible=False
    return possible    
    