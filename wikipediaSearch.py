import wikipedia
from wikipedia.exceptions import DisambiguationError

'''
    Author: Carlos Eduardo
    Last Update: 11/19/2020
'''

# --- Wikipedia Class to Search and Environment --- #
class Wikipedia:
    def search(search):                  
        try:
            wikipedia.set_lang("pt")  
            result = wikipedia.summary(wikipedia.search(str(search))[0])            
            return result

        except DisambiguationError as error: 
            print(error)
            pass