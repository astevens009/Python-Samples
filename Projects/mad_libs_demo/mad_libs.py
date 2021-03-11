import random

# NOTE: Randomly select a text to display prompting the user to choose the appropriate word type.

libs = {
    0: ["verb", "I like my donuts with extra {} in them."],
    1: ["noun", "What came first, the chicken or the {}?"],
    2: ["adjective", "Flip-flops ara a staple of any {} summer wardrobe."],
    3: ["noun", "BBQ at my house! Everyone's invited,a nd it's Bring Your Own {}"],
    4: ["adjective", "Once that {} music comes on, it's time to shut down your acceptance speech!"],
    5: ["plural noun", "One jelly donut with whipped cream and extra {}, please."]
}

keep_playing = 'Y'

# TODO: Display a description of each word type (i.e. - "a verb is an action word"; "a noun is a thing"; etc)

while keep_playing == 'Y' or keep_playing == "YES":
    # TODO: Randomly select a mad lib
    lib_key = random.randint(0, len(libs)-1)

    # TODO: Retrieve the appropriate mad lib
    mad_lib = libs[lib_key]

    # TODO: Prompt the user for the appropriate word type (verb, noun, etc.)
    word_type = input("\nPlease select a {} : ".format(mad_lib[0]))

    # TODO: Replace the place holder with the user's input 
    print("Your Mad Lib is: \n\n\t{}\n"
        .format(mad_lib[1].format(word_type.upper())))

    keep_playing = input("Would you like to play again? (Y/N): ").upper()

# TEST
# print(lib_key)
# print(mad_lib[1])
