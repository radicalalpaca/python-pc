import os
import time

current_directory = os.getcwd()
print(current_directory)

os.mkdir('newDir')

time.sleep(2)
os.rename('newDir', 'newDir2')
time.sleep(2)
os.rmdir('newDir2')