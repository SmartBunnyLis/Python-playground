# Assignment: Stars
# Write the following functions.
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(x):
    for i in x:
        if type(i) is str:
            print i[0].lower() * len(i)
        else:
            print "*" * i

draw_stars(x)

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed
# to the draw_stars() function. When a string is passed, instead of displaying *,
# display the first letter of the string according to the example below.
# You may use the .lower() string method for this part.
