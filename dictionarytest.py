import json
from difflib import get_close_matches
data=json.load(open("data.json",'r'))
def translate(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word,data.keys()))>0:
        similar=input("Do you mean %s instead. if yes press y if no press n" % get_close_matches(word,data.keys())[0])
        if similar=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif similar=='n':
            return "The word you are looking for doesnt exist."
        else:
            return "unrecognizable."
    else:
            return("The word doesnt exist, Please double check it")
word=input("What are you looking for?")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
