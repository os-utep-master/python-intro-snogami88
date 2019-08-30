import os         #Checks if file exists
import re         #regualr expression 
import sys        #command line areguments
import subprocess #executing program

if(len(sys.argv) is not 3):
    print("Correct Syntax: wordCount.py <input_file.txt> <output_file.txt>")
    exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

#Check if input file exists
if not os.path.exists(input_file_name):
    print("input text file %s does not exists!" % input_file_name)
    exit()

#Check if output file exists
if not os.path.exists(output_file_name):
    print("output text file %s does not exists!" % output_file_name)
    exit

#Read the file
def read_file(input_file):    

#Print output file, or overide existing file
def create_file(final_list):

#Create a list of words case insesitive and count
def create_list(file_info):
    
#Filter the words and count into alphabetical order
def organize(word_list):





file_info = read_file(input_file_name)
word_list = create_list(file_info)
word_list = organize(word_list)
create_file(word_list)
print("Information from %s has been seperated into a list posted in %s" (input_file_name, output_file_name)

