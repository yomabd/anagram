#python3
#@created by yomabd

#Define anagram detector function
# from os import remove


def is_anagram(string, anagram):

    string_list = list()
    anagram_list = list()
    #cleansing the two strings off non-letter characters and
    # make lists of pure letters
    for character in string:
        if character.isalpha():
            string_list.append(character.lower())
            
    for character in anagram:
        if character.isalpha():
            anagram_list.append(character.lower())
            
    print(string_list," ",anagram_list)

    match_detector = 0
    for x in string_list:
        for y in anagram_list:
            if x == y:
                match_detector = 1
                anagram_list.remove(y)
                break
        if match_detector == 0:
            return 'False'
    return 'True'
      
    
        

print(is_anagram('the country side','no city-dust here'))
