import json
from difflib import get_close_matches
jsonfile=json.load(open(data.file))
word = input("enter your word:")
    def check(d):
          d=d.lower
          if d in jsonfile:
              return jsonfile[d]
          elif len(get_close_matches(d,jsonfile.keys()))>0:
              choice = input("did you mean %s",Enter y for yes,Enter n for no,)%get_close_matches(d,jsonfile.keys([0])
          if choice == 'Y' or 'y':
              return %get_close_matches(d,jsonfile.keys()[0])
          elif choice == 'N' or 'n':
              return "the word doesn't exist","please try another word"
          else:
              return "the word doesn't exist","please try another word"
result = check(word)
          if type(result) == list:
              for i in result:
                  print(i)
          else:
              print(result)
