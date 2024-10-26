# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    set1 = first[0:1]
    set2 = mid[0:1]
    set3 = last[0:1]
    personsInitials = set1 + ". " + set2 + ". " + set3 + "."
    print(personsInitials)

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)
