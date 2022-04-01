#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess
import time


##check if the rich module exists, if not, install it
try:
    from rich import print
    from rich import pretty
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "rich"])
    import rich
    time.sleep (1)
     #tell the user the library is installed
    print("[!] Rich module is now installed")
    print("Please restart the program")
    time.sleep(3)
    sys.exit()



line_list = []

#print the name and contents of the current directory
def print_dir_contents(path):
    print("\nCurrent Directory: [blue]" + path + "[blue]")
    print("\nDirectory Contents:")
    for item in os.listdir(path):
        print("[cyan]"+ item + "[/cyan]")

#call the print_dir_contents function to print the contents of the current directory
print_dir_contents(os.getcwd())

#Ask the user to pick a file to search from
def get_file_to_search():
    print("\nPlease select a file to search:")
    #while loop to make sure the user enters a valid file
    while True:
        file_to_search = input("\nEnter file name: ")
        if os.path.isfile(file_to_search):
            return file_to_search
        else:
            print("\n[yellow bold]Invalid file name. Please try again.[/yellow bold]")

#call get_file_to_search function to get the file to search
file_to_search = get_file_to_search()

#search the file for a pattern, and return the contents of the line the matches the pattern
def search_file(file_to_search):
    #Ask the user to enter a pattern to search for
    print("\nPlease enter a pattern to search for:")
    pattern = input("\nEnter pattern: ")
    #open the file to search
    with open(file_to_search) as f:
        #read the file line by line
        for line in f:
            #for each line, check if the pattern is in the line, if it is append the line to the line_list
            if pattern in line:
                line_list.append(line)
    #return the line_list and the value of pattern
    return line_list, pattern

#create a function that removes the pattern "\n" from the line_list
def remove_newline(line_list):
    #for each line in the line_list, remove the "\n"
    for i in range(len(line_list)):
        line_list[i] = line_list[i].rstrip()
    return line_list

#Ask the user if they want to call the search_file function
print("\nWould you like to search the file for a pattern?")
search_file_answer = input("\nEnter 'y' for yes, or 'n' for no: ")
#if the user enters 'y', call the search_file function
while search_file_answer != 'n':
    #call the search_file function
    line = search_file(file_to_search)
    #print the lines that match the pattern
    print("\nThe following lines match the pattern:\n")
    #call the remove_newline function
    remove_newline(line_list)
    #get the value of pattern from the search_file function
    pattern = line[1]
    for line in line_list:
        print("[italic green]"+ line + "[/italic green]")
    #save the line_list to a file
    with open("search_results.txt", "a") as f:
        #add the date and time to the file
        f.write("\n" + time.strftime("%c"))
        f.write("\nPattern searched for: " + pattern + "\n")
        for line in line_list:
            f.write(line + "\n")
        f.write("\n------------------------------------------------------")
    #Ask the user if they want to search again
    print("\nWould you like to search the file for a pattern?")
    search_file_answer = input("\nEnter 'y' for yes, or 'n' for no: ")
    if search_file_answer == 'n':
        break

print("Please see the search_results.txt file for a list of the results")

#Create a countdown timer that prints the time every second until the timer reaches 0
def countdown_timer():
    #set the timer to 10 seconds
    timer = 3
    #while loop to run the timer
    while timer > 0:
        #print the timer every second
        print("\n[cyan]" + str(timer) + "[/cyan]", end="".rstrip("\n"))
        time.sleep(1)
        #decrement the timer by 1
        timer -= 1

#Say the to the user that program will exit in 3 seconds, call the countdown_timer function
print("\n[yellow]Program will exit in 3 seconds.[/yellow]")
countdown_timer()
sys.exit()