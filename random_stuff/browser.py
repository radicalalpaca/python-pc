import os
import sys
import requests
from bs4 import BeautifulSoup

dir = sys.argv[1]
if not os.path.exists(dir):
    os.mkdir(dir)
my_stack = []

def load():
    global content
    global r
    r = requests.get(f'https://{user_input}')
    content = r.text

def save():
    with open(f'{dir}\\{saved_url}.txt', 'w', encoding=r.encoding) as save:
        save.write(content)
    my_stack.append(content)
    
def read():
    with open(f'{dir}\\{user_input}.txt', 'r') as read:
        print(read.read())
    my_stack.append(user_input)
    

while True:
    user_input = input("entry: ")
    saved_url = user_input[:-4]
    if "." in user_input:
        load()
        save()
        print(content)
    elif user_input == "back" and len(my_stack) == 0:
        pass
    elif user_input == "back" and len(my_stack) == 1:
        if "<!DOCTYPE html>" not in my_stack.pop(): 
            with open(f'{dir}\\{my_stack[-1]}.txt', 'r') as f:
                print(f.read())
        else:
            print(my_stack.pop())
    elif user_input == "back":
        if "<!DOCTYPE html>" not in my_stack.pop():
            with open(f'{dir}\\{my_stack.pop()}.txt', 'r') as f:
                print(f.read())
        else:
            print(my_stack.pop())
    elif user_input == "exit":
        break
    elif "." not in user_input:
        read()
    else:
        print("error")