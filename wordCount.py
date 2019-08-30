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

#Check if input file exists
if not os.path.exists(input_file_name):
    print("input text file %s does not exists!" % input_file_name)
    exit()

#Check if output file exists
if not os.path.exists(output_file_name):
    print("output text file %s does not exists!" % output_file_name)
    exit()

#Read the file    
with open(input_file_name, 'r') as inputF:      #open and read the file then close
    word_list = inputF.read()                   #Read the complete file
    word_list = word_list.lower()            #Do not compare the case tense
    word_list = re.split('\W+', word_list)    #split into array of anything that is not a word
    word_list = sorted(set(word_list))          #Put list in alphabetical order becoms 
print(word_list)
 

#Create array with count of each words
count = count[len.word_list]
i = 0
prev = ""
for index in word_list:
    count[i] = count[i] + 1
    if prev != index:
        i = i + 1
    prev = index
print(count)

#Print output file, or overide existing file
with open(output_file_name, 'w') as inputOut:   #open file write and close file
    i = 0
    for e in word_list: 
        inputOut.write("%s %d\n" % (e, count[i]))
        i = i + 1

print("Information from %s has been seperated into a list posted in %s" % (input_file_name, output_file_name))

