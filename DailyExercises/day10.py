"""
The code below is incomplete. It should calculate and print out the maximum value of the grades list.
Please complete the function and then call it.


"""

def get_max(grades):
    maxVal = grades[0]
    for item in grades:
        for comparedTo in grades:
            if maxVal < comparedTo:
                maxVal = comparedTo

    return(maxVal)


def get_both(grades):
    maxVal = get_max(grades)
    minVal = grades[0]
    for item in grades:
        for comparedTo in grades:
            if minVal > comparedTo:
                minVal = comparedTo
    print(f"max: {maxVal}, min: {minVal}")



grades = [9.6, 9.2, 9.7, 10.0, 2.0]
print(get_max(grades))
get_both(grades)
