#Define a function contains_blue() that accepts any number of arguments. It should return True if any of the arguments are "blue" (all lowercase). Otherwise, it should return False .

desired = "blue"
list = 0
ELVIS = ("Love Me Tender", 1935, "Blue suede shoes", "Blue Hawaii")
elvis = str (ELVIS)
elvis = elvis.lower()
Emily = "Emily Brontë, \‘The Blue Bell\’. The blue bell is the sweetest flower That waves in summer air; Its blossoms have the mightiest power To soothe my spirit\'s care."
EMILY = str (Emily)
EMILY = EMILY.upper()
beginning = ("Bluebell", 12345, True, 99)
middle = "abcdblueefgh"
end = "the_end_of_this wordisblue"

def contains_blue(desired, list):
    if desired in list:
        print ("True")
    else: print ("False")

list = ELVIS
contains_blue (desired, list)

list = elvis
contains_blue (desired, list)

list = Emily
contains_blue (desired, list)

list = EMILY
contains_blue (desired, list)

list = beginning
contains_blue (desired, list)

list = middle
contains_blue (desired, list)

list = end
contains_blue (desired, list)


