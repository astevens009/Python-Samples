def get_acronym(phrase_list):
    # print("TEST: {}".format(phrase_list))

    acronym = ""

    # Strip off the first letter of each word
    for word in phrase_list:
        if word not in ["a", "an", "the", "of"]:
            # In the special case of the word "without" the initials 
            # should always be 'W' and 'O'
            if word.casefold() == "without":
                acronym += "W.O."
            else:
                # Otherwise just append the first letter of each # word to the acronym
                acronym += word[0] + "."

            # print("TEST: Initials - {}".format(initials))
    
    return acronym

phrase = input("\nPlease type in a phrase or full organizational name:\n")

phrase_list = phrase.split()
print("\nThe acronym for \"{}\" is {}\n".format(phrase, get_acronym(phrase_list)))
