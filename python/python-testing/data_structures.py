"""
Making a dictionary about myself
"""

lilly = {"name": "Lilly", "age": 18, "gender": "female", "num_siblings": 1,
    "books": ["East of Eden", "Signs Preceeding the End of the World", "Beloved"]}

print lilly

for key in lilly.keys():
    if(key=="age"):
        print "you are an adult!!!"
