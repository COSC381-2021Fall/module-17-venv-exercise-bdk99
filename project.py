import emoji    #Installed Using PIP  
import pyjokes  #Installed Using PIP
import snowjob  #Installed Using PIP
import os
import time

print("Displaying Christmas Tree Emoji in 2 seconds!")
time.sleep(2)
print(emoji.emojize(":Christmas_tree:"))
print("Displaying pyjoke in 2 seconds!")
time.sleep(2)
os.system("pyjoke")
print("Displaying snow in terminal in 5 seconds!")
time.sleep(5)
os.system("snowjob")