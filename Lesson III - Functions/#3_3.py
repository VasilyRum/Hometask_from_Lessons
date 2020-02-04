def average_stil_max(a, b, c, d):
    """
return the arithmetic mean of the arguments
and the largest argument for the entire time
 of calls to this function
    """
    average = (a + b + c + d) / 4
    if not hasattr(average_stil_max, '_state'):
        average_stil_max._state = 0
    if average_stil_max._state < max(a, b, c, d):
        average_stil_max._state = max(a, b, c, d)
    return average, average_stil_max._state

print(average_stil_max(1, 2, 3, 45))
print(average_stil_max(1, 2, 3, 11))
print(average_stil_max(1, 2, 3, 12))
print(average_stil_max(1, 2, 3, 100))
print(average_stil_max(1, 2, 3, 10))
