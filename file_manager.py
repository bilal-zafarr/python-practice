import os
import random

current_path = os.getcwd()

def list_current_directory():
    files = [f for f in os.listdir(current_path) if os.path.isfile(f)]
    directories = [d for d in os.listdir(current_path) if os.path.isdir(d)]
    print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")
    print("\t****files****")
    for f in files:
        print (f)
    print("\t****directories****")
    for d in directories:
        print(d)
    print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

def check_if_file_exisis(file):
    files = [f for f in os.listdir(current_path) if os.path.isfile(f)]
    if file in files:
        return True
    return False

def check_if_dir_exisis(dir):
    dirs = [d for d in os.listdir(current_path) if os.path.isdir(d)]
    if dir in dirs:
        return True
    return False

def make_name_random(name):
    return name+str(random.randrange(1,1000))


def create_file():
    file_name = input("\nEnter the name of file you want to create/ or enter 0 to return to the main menu: ")
    if(file_name!= "0"):
        notification = False
        while(check_if_file_exisis(file_name)):
            notification = True
            file_name = make_name_random(file_name)
        try:
            f = open(f"{current_path}/{file_name}", "w")
            if(notification):
                print("\n################")
                print(f"A file with the name you enterd already exists. \nYour new file has been created with the name \"{file_name}\"")
                print("################\n")
        except:
            print("An error occured while trying to create the file")
    
    
def create_directory():
    dir_name = input("\nEnter the name of directory you want to create/ or enter 0 to return to the main menu: ")
    if(dir_name!= "0"):
        notification = False
        while(check_if_dir_exisis(dir_name)):
            notification = True
            dir_name = make_name_random(dir_name)
        try:
            os.mkdir(f"{current_path}/{dir_name}")
            if(notification):
                print("\n################")
                print(f"A directory with the name you enterd already exists. \nYour new file has been created with the name \"{dir_name}\"")
                print("################\n")
        except OSError as error:
            print(error)

def remove_file():
    file_to_remove = input("\nEnter the name of file you want to remove/ or enter 0 to return to the main menu: ")
    if(file_to_remove!= "0"):
        try:
            os.remove(f"{current_path}/{file_to_remove}")
        except OSError as error:
            print(error)

def remove_directory():
    dir_to_remove = input("\nEnter the name of directory you want to remove/ or enter 0 to return to the main menu: ")
    if(dir_to_remove!="0"):
        try:
            os.rmdir(f"{current_path}/{dir_to_remove}")
        except OSError as error:
            print(error)

def change_path():
    new_path = input("\nEnter the new path/ or enter 0 to return to the main menu: ")
    if(new_path!="0"):
        if os.path.exists(new_path):
            global current_path
            current_path = new_path
        else:
            print("\n***Path could not be changed. Check if path exists***")

def main():
    print("\n-> Enter 1 to list the current directory")
    print("-> Enter 2 to create a file in the current directory")
    print("-> Enter 3 to create a new directory")
    print("-> Enter 4 to remove the file")
    print("-> Enter 5 to remove the directory")
    print("-> Enter 6 to lsit the current absolute path")
    print("-> Enter 7 to move to the desired absolute path")
    print("-> Enter any other key to exit the program\n")
    print("------------------------------------------------")

    choice = input("Your Choice: ")

    if choice == "1":
        list_current_directory()
    elif choice == "2":
        create_file()
    elif choice == "3":
        create_directory()
    elif choice == "4":
        remove_file()
    elif choice == "5":
        remove_directory()
    elif choice == "6":
        print("\n" + current_path)
    elif choice == "7":
        change_path()
    else:
        exit()

if __name__ == "__main__":
    print("\n------------------------------------------------")
    print("\tWelcome to Python file manager")
    print("------------------------------------------------")
    while True:
        main()
