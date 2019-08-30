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
count = []

#Check if input file exists
if not os.path.exists(input_file_name):
    print("input text file %s does not exists!" % input_file_name)
    exit()

#Check if output file exists
if not os.path.exists(output_file_name):
    print("output text file %s does not exists!" % output_file_name)
    exit

#Read the file
def read_file():    
    with open (input_file_name, 'r') as inputF           #open and read the file then close
        word_list = inputF.read()                   #Read the complete file
        word_list = word_list.casefold()            #Do not compare the case tense
        word_list = word_list.split()               #Remove any next line spaces
        word_list = re.split('[\W+]', word_list)    #split into array of anything that is 
        word_list = sorted(set(word_list))          #Put list in alphabetical order
        print(word_list)
    return word_list

#Print output file, or overide existing file
def create_file(final_list, num_list):
    with open (output_file_name, 'w') as inputOut
        for e in final_list
            print("%s %d\n", (final_list, num_list))  

#Create array with count of each word
def get_count(words):
    i = 0
    prev = ""
    for index in words:
        if prev != index:
            i++
        count[i] = count + 1
        prev = index
        

word_list = read_file()
count = organize(word_list)
create_file(word_list, count)
print("Information from %s has been seperated into a list posted in %s" (input_file_name, output_file_name)

