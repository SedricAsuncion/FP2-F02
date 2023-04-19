#-----------------------------
#Writing_Files.py
#Sedric Asuncion
#-----------------------------

## ----- Import ----- ##
import random

## ----- Functions ----- ##
def creation():
    #cretes a file in Writing Mode
    file = open('scores_file.txt', 'w')
    
    #writes the starting strings
    file.write('Document Opened in North America')
    file.write('\nWelcome, First User')
    file.write('\nThis is where your highscres will be recorded:')
    
    #closes file (important to close)
    file.close()
    
def list_highscores():
    #opens file in Append Mode
    listing = open('scores_file.txt', 'a')
    
    #generates random 'scores' and appends them to file
    score = random.randint(1,100)
    listing.write(f'\n{score}')
    
    #closes file
    listing.close()

def read_print():
    #opens file in Reading Mode
    read = open('scores_file.txt', 'r')
    
    read_all = read.read()
    
    #prints all data inside file
    print(read_all)
    
    #closes file
    read.close()
    
def main():
    creation()
    list_highscores()
    list_highscores()
    list_highscores()
    read_print()
        
## ----- Main Code ----- ##
main()
    
    