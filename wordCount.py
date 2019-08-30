import os         #Checks if file exists
import re         #regualr expression 
import sys        #command line areguments
import subprocess #executing program

if(len(sys.argv) is not 3):
    print("Correct Syntax: wordCount.py <input_file.txt> <output_file.txt>")
    exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
word_list = []
sorted_list = []
word_dictionary = {}
#Check if input file exists
if not os.path.exists(input_file_name):
    print("input text file %s does not exists!" % input_file_name)
    exit()

#Read the file    
with open(input_file_name, 'r') as inputF:        #open and read the file then close
    word_list = inputF.read()                     #Read the complete file
    word_list = word_list.lower()                 #Do not compare the case tense
    word_list = re.split('\W+', word_list)        #split into array of anything that is a word
    sorted_list = sorted(set(word_list))          #Put list in alphabetical order 
    word_list = tuple(word_list)                  #Create list into tuple

#Print output file, or overide existing file
#with open(output_file_name, 'w') as inputOut:   #open file write and close file
#    for e in sorted_list:                       #traverse the each link of list
#        num = word_list.count(e)                #get total occurances of word in list
#        if(len(e)>=1):                          #Bug empty space
#            inputOut.write("%s %d\n" % (e, num))    #write to file

                
#Print output file, or overide existing file
with open(output_file_name, 'w') as inputOut:   #open file write and close file
    for e in sorted_list:                       #traverse the each link of list
        num = word_list.count(e)                #get total occurances of word in list
        if(len(e)>=1):                          #Bug empty space
            word_dictionary[e] = num            #Create New dictionary entry
    for word, number in word_dictionary.items():    #traverse dictionary
        inputOut.write("%s %d\n" % (word, number))  #Write to file from dictionary