import os
if __name__ == '__main__':

    print("Welcome to your speaker")
    x= input("Enter what you want me to say: ")
    command = f"say{x}"
    os.system(command)
