'''Implement a progarm that calculates the standard weight

Male: height x height x 22
Female: height x height x 21

condition1: Use a method to calculates the standard weight
            method name: std_weight
            parameter: height, gender
condition2: Represent the weight till two decimal digits'''

def std_weight(height, gender): 
    weight = 0.00

    if gender.lower() == "male":
        weight = round(height*height*22/10000, 2)
        print("{0}cm male's standard weight is {1}".format(height, weight))
    elif gender.lower() == "female":
        weight = round(height*height*21/10000, 2)
        print("{0}cm female's standard weight is {1}".format(height, weight))
    else:
        print("Please check the Gender information")
    

std_weight(175, "Male")
std_weight(165, "Female")
