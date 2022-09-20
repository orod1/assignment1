

#this will check to make sure the word is legitimate
def validate_input(user_input):

    user_input = user_input.strip().lower()

    if user_input != None and user_input != "":
        return True
    else:
        print("Please enter a word: ")
        return False


#checks if the word in the list is an anagram of the input word
def is_word_anagram(word, user_input):
    #go through each letter of the input and if it is in the data word, 
    #       then remove it from the date word

    for letter in user_input:
        if letter in word:
            word.remove(letter)
        
    #if all letters have been removed from the data word,
    #       then it is an anagram
    if len(word) == 0:
        return True
    else:
        return False



#this will go through the list of anagram words and display them in order of word length
def print_grouped_words(anagram_list):
    #go down from 6 letter words to 3
    for i in range (6, 2, -1):
        print("List of " + str(i) + " letter words:")

        for word in anagram_list:
            #checks if the word is the correct length
            if len(word) == i:
                print(word)
        
    



#open words file
file = open('words.txt')

#read the file into a list
data = file.readlines()

#this will be what we put the anagrams into
anagram_list = []

user_input = input("Please enter a word: ")

if validate_input(user_input):
    
    for word in data:
        #cleaning the word
        word = word.strip().lower()

        #checks if the word is between 3-6 letters
        # we dont need to check for words beyond this range
        if len(word) >= 3 and len(word) <= 6:
            
            if is_word_anagram(sorted(word), sorted(user_input)):
                #add word to the anagram list
                anagram_list.append(word)


print("Here are the anagram words:")

print_grouped_words(anagram_list)





