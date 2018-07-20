"""Making the Mad Libs Lab"""
noun1 = input('Give me a noun: ')
noun2 = input('Give me a noun: ')
adjective1 = input('Give me an adjective: ')
verb1 = input('Give me a participle verb: ')

print("The {noun1} jumped over a {adjective1} {noun2}. Then the {noun2}"
    "decided to stop being so {adjective1} and take up a hobby: {verb1}".format(
        noun1 = noun1, adjective1 = adjective1, noun2 = noun2, verb1 = verb1))
