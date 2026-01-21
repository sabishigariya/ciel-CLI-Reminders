import tkinter as tk
import os
import json

yellow = "\033[1;33m"
red = "\033[1;31m"
bright_white = "\033[1;0m"

def Clear_Screen():
     if os.name == 'nt':
          os.system('cls')
     else:
          os.system('Clear')

To_Do_List = []
Title_List = []
# this is for make codes to understand and easy to distinction the months
Month_31 = (1,3,5,7,8,10,12)
Month_30 = (4,6,9,11)
Month_29 = (2,)
# I got help from chatgpt to how to use Json, and fix my codes at here:
# By using Json to load the file of saved Lists of "To_Do_List" and "Title_List"
try:
    if os.path.exists("To_Do_List.json"):
        with open("To_Do_List.json", "r", encoding="utf-8") as f:
            To_Do_List = json.load(f)

    if os.path.exists("Title_List.json"):
        with open("Title_List.json", "r", encoding="utf-8") as f:
            Title_List = json.load(f)

    print("Loading complete:")
# if there is an error of the code cannot load the file, print an error massage for that
except Exception as e:
    print(f"Sorry I could not load the save: {e}")
    
def Show_list():
    print("\n", To_Do_List, "\n")

def Add():
    global What
    print('please input what you have to do or want to do?')
    What = input("What do you have to do? or Title this: ")
    Title_List.append (What)

    Year = input_Year()
    Month = input_Month()
    Date = input_Date()
# While I was strugle with date check codes, I asked Chatgpt to what was the problem of it, and it said
# I used  lot of "if" and "def" functions to make python also myself confuse what is going on
# And chatgpt remake this while loop with simpler codes
    while True:
        if Year == 2025 and Month <= 11:
            Clear_Screen()
            print(red+"if you are going to input Month and Date in 2025, please input Month later than 11 because it's almost end"+bright_white)
            Year = input_Year()
            Month = input_Month()
            Date = input_Date()

        elif Month in Month_31 and not (1 <= Date <= 31):
            Clear_Screen()
            print(red+"impossible value to put in Date"+bright_white)
            Month = input_Month()
            Date = input_Date()

        elif Month in Month_30 and not (1 <= Date <= 30):
            Clear_Screen()
            print(red+"impossible value to put in Date"+bright_white)
            Month = input_Month()
            Date = input_Date()

        elif Month in Month_29 and not (1 <= Date <= 29):
            Clear_Screen()
            print(red+"impossible value to put in Date"+bright_white)
            Month = input_Month()
            Date = input_Date()

        else:
            break
# Use if and while loop to make repetition for input the correct value for time
# and distinction when user input a numbers for time or they even not input any value for it
    print("Please input with 24-hour clock (0 ~ 23)")
    Time = (input("until what time? (optional): "))
    if Time == (""):
        Time = ("")
    else:
        Time = int(Time)
        while True:
         if Time < 0 or Time > 23:
            print()
            Time = int(input("until what time? (optional): "))
         else:
            break
# when they inputted a value with number and it is available, put ":00" to make look natural
        Time = (f"{Time}:00")

    New_todo = (f"{What} ,{Month}""/"f"{Date},{Year},{Time}")
    To_Do_List.append (New_todo)
    print("\n", To_Do_List, "\n")
# make all of inputs(When) with "def" to I could easy to put the codes again, and makes easy to repeat     
def input_Month():
    print("Please input a value for Month")
    try:
        Month = int(input("When? (month): "))
    except:
        print(red+"Cannot cast Month to int"+bright_white)
        return input_Month()
    if Month < 1 or Month > 12:
        print(red+"impossible value to put in Month"+bright_white)
        return input_Month()
    else:
        print("accepted value in Month")
        return Month

def input_Date():
    print("Please input a value for Date")
    try:
        Date = int(input("When? (Date): "))
    except Exception:
        print(red+"Cannot cast Date to int"+bright_white)
        return input_Date()
    if Date <= 0 or Date > 31:
        print(red+"impossible value to put in Date"+bright_white)
        return input_Date()
    else:
        print("accepted value in Date")
        return Date

def input_Year():
    print("Please input a value for year")
    try:
        Year = int(input("When? (year): "))
        if Year < 2025:
          print(red+"please don't input before 2025 in Year because it's already passed"+bright_white)
          return input_Year()
        elif Year >= 2125:
          print(red+"please don't input after than 2125 in Year because I don't think you could alive"+bright_white)
          return input_Year()
        else:
          print("accepted value in Year")
          return Year
    except Exception:
        print(red+"Cannot cast Year to int"+bright_white)
        return input_Year()
# make a list of Title/name that user named to make users to easier to input, and 
# make codes simpler for searching the schedules        
def Remove():
    print("Which plan do you remove from the List, please input the title of that plan")
    find_title = input("> ")
    try:
        index_of_find = Title_List.index(find_title)
        To_Do_List.remove(To_Do_List[index_of_find])
        Title_List.remove(Title_List[index_of_find])
        print("\n", To_Do_List, "\n")
    except Exception:
        print(red+f"There is not name '{yellow+find_title+red}' in the list of plan"+bright_white)
        print("Please input again")
        Remove()
def Close():
    print(yellow+"See you"+bright_white)
    print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡴⠒⠚⣻⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠓⠒⠒⠒⠒⢤⣤⠴⠚⠉⠀⡸⠁⣠⠞⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⣠⠖⠋⠀⠀⠀⠀⢀⡧⠞⠣⠤⣀⡀⠀⠀⠀⠀
⢀⣤⠔⠒⠚⣏⠉⠉⠉⠉⠉⠉⠉⠒⠒⠲⠤⠒⠋⠉⠉⠉⠉⠉⠒⠒⠻⢴⠋⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠉⠑⠲⢤⡀
⠈⠙⠒⠤⢄⣘⣦⡀⠀⠀⠀⠀⠀⠀⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠀⠀⠈⢉⣿⣗⡒⠒⠒⡾⠁⣠⣶⠒⡆⠀⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀
⠀⠀⠀⠀⠀⠀⢠⡎⠀⠀⠙⢦⣀⠇⠀⠻⣼⡿⠁⠀⠀⢠⡄⠀⠀⠸⣷⣼⣷⠀⢸⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣏⠀⠀⠀⠀⡿⠖⠲⣄⠀⠀⣤⡀⢀⣤⣀⠀⠀⢀⠈⠋⠁⠀⢸⣿⡉⠓⠦⣀⡀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⡇⠀⠀⣸⠀⠀⢸⣯⠟⠛⠛⢿⣿⠋⠀⢰⠟⠉⠹⡇⢷⠀⠀⠀⠉⠓⠦⣄⣠⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠹⡦⠴⠋⠀⠀⠀⢹⡄⠀⢀⡼⠁⠀⠀⣇⠀⠀⢠⡇⣀⣧⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠙⢆⠀⠀⠀⠀⠀⠹⠤⠋⠀⠀⠀⠀⠈⠓⡶⠋⠙⠳⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠑⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠖⠋⠀⠀⠀⠀⠀⠀⠉⠲⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⠀⢀⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠤⣤⠤⠴⠒⠒⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡆⢀⣠⠤⠒⠒⠒⠂⠀⠀⠐⠒⠒⠒⠒⠲⢦⡀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠒⠾⠀""")
   # at this point, when user click the button of "Close", this codes make a file to save the lists 
    try:
        with open("To_Do_List.json", "w", encoding="utf-8") as f:
            json.dump(To_Do_List, f, ensure_ascii=False, indent=2)

        with open("Title_List.json", "w", encoding="utf-8") as f:
            json.dump(Title_List, f, ensure_ascii=False, indent=2)

    except IOError as e:
        print(f"Sorry I could not save it: {e}")
    root.destroy()
    
root = tk.Tk()
root.title("schedule calendar")
Button_List = tk.Button(root, text="List", command=Show_list)
Button_List.pack()

Button_Add = tk.Button(root, text="Add schedule", command=Add)
Button_Add.pack()

Button_Remove = tk.Button(root, text="Remove schedule", command=Remove)
Button_Remove.pack()

Button_Close = tk.Button(root, text="close", command=Close)
Button_Close.pack()

root.mainloop()