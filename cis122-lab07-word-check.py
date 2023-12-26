'''
CIS 122 Fall 2021
Author: Liam Bouffard
Objective:  prompt the user for input, exit if nothing entered, 
    or search through the list of words to determine if the word 
    (case insensitive) is found
'''
# step 1: input
while 2 != 4:
    word = input('Enter a search word (blank to exit): ')
    word = word.strip()
    if len(word) == 0:
        # Exit if nothing entered
        break
    else:
        fin = open('words_alpha.txt')
        
        # Search for word by looping over file

        # Initialize default search result to False
        word_found = False
        for line in fin:
            # remove file line leading/trailing white space and line endings
            line = line.strip()

            # Test for match changing to same case
            if word.upper() == line.upper():
                
                # Set result status and exit loop
                word_found = True
                break

    # close file
    fin.close()

    # print results
    if word_found:
        print('Word ' + word + ' found')
    else:
        print('Word ' + word + ' not found')
    