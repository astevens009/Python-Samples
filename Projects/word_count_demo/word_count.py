print("\nPlease respond to the question and I will count the number of words in your response.\n")
word_list = input("What is on your mind today?: ").split()

print("The number of words in your response is: {}.\n"
.format(len(word_list)))