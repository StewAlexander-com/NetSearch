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

#Try to upgrade the rich module
try:
    subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "rich"])
    time.sleep(10)
    import rich
except:
    pass

line_list = []

print('''[yellow bold]
 _   _      _   ____                      _
| \ | | ___| |_/ ___|  ___  __ _ _ __ ___| |__
|  \| |/ _ | __\___ \ / _ \/ _` | '__/ __| '_ \ 
| |\  |  __| |_ ___) |  __| (_| | | | (__| | | |
|_| \_|\___|\__|____/ \___|\__,_|_|  \___|_| |_|
[/yellow bold]''')

print('''[bright_cyan]
┌──────────────────────────────────────────────────┐
│  [white]Searches a MAC or IP ARP Table for a string[/white]     │
│  [white]or strings, and saves the results with a time[/white]   │
│  [white]stamp to a file[/white]                                 │
└──────────────────────────────────────────────────┘
[bright_cyan]''')


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
    #clear line_list
    line_list.clear()
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

#call the remove_newline function to remove the "\n" from the line_list
remove_newline(line_list)

#Create a function that takes the line_list and pattern and saves the results to a file
def save_results(line_list, pattern):
    #call the function to remove the "\n" from the line_list
    remove_newline(line_list)
    #create a file name "search_results.txt"
    file_name = "search_results.txt"
    with open(file_name, "a") as f:
        #print the current date and time
        f.write("\n\nResults of " + pattern + " saved at: " + time.strftime("%c") + "\n")
        #for each line in the line_list, save the line to the file
        for line in line_list:
            f.write(line + "\n")
    #close the file
    f.close()
    #print the contents of the file
    with open(file_name) as f:
        print("\n\n[cyan]File contents:[/cyan]")
        for line in f:
            print(line, end="")
    #close the file
    f.close()


#Call the search_file function to search the file for a pattern
line_list, pattern = search_file(file_to_search)
#call the save_results function to save the results of the search
save_results(line_list, pattern)

#While the answer is not "n", ask the user if they want to search the file again
answer_search_again = "y"
while answer_search_again !="n":
    #Ask the user if they want to search the file again
    print("\n\n[yellow]Search again, y/n?[/yellow]")
    answer_search_again = input("> ")
    #if the answer is "y", call the search_file function to search the file for a pattern
    if answer_search_again == "y":
        line_list, pattern = search_file(file_to_search)
        #call the save_results function to save the results to a file
        save_results(line_list, pattern)
    #else pass
    else:
        pass

print("\n[yellow]===[/yellow] Please see the [cyan italic]search_results.txt[/cyan italic] file for a list of the results [yellow]===[/yellow]")

#Create a countdown timer that prints the time every second until the timer reaches 0
def countdown_timer():
    #set the timer to 10 seconds
    timer = 3
    #while loop to run the timer
    while timer > 0:
        #print the timer every second
        print("[cyan]" + str(timer) + "[/cyan]", end=" ".rstrip("\n"),)
        time.sleep(1)
        #decrement the timer by 1
        timer -= 1
    print("...", end="".rstrip("\n"))
#Say the to the user that program will exit in 3 seconds, call the countdown_timer function
print("\n[yellow]Program will exit in 3 seconds.[/yellow]")
countdown_timer()
sys.exit()