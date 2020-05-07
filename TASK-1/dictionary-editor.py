import re

def add_word():
    new_word=input("Enter the new word:")
    
    file = open('dictionary.txt','r')
    file_content = file.read()
    file.close()
    
    words = file_content.split('\t')
    
    for word in words:
        if word==new_word:
            print(f'{new_word} already exists in dictionary.')
            break
    else:
        file = open('dictionary.txt','a+')
        file.write(new_word+'\t')
        file.close()

        
def search():
    search_word = input("Enter the characters of the word to be searched:")
    
    file = open('dictionary.txt','r')
    file_content = file.read()
    file.close()
    
    words = file_content.split('\t')
    
    for word in words:
        if search_word in word:
            print(word)
            

def change_spell():
    wrong_word=input("Enter the mis-spelled word:")
    correct_word=input("Enter the correct word:")
    word_list = []
    
    file = open('dictionary.txt','r+')
    file_content = file.read()
    file_content = re.sub(wrong_word,correct_word,file_content)
    file.seek(0)
    file.write(file_content)
    file.truncate()
    
    
def delete():
    delete_word=input("Enter the word to be deleted:")
    
    file = open('dictionary.txt','r+')
    file_content = file.read()
    file_content = re.sub(delete_word,'',file_content)
    file.seek(0)
    file.write(file_content)
    file.truncate()
            

def sorted_list():
    file = open('dictionary.txt','r')
    file_content = file.read()
    file.close()
    
    word_list = []
    
    words = file_content.split('\t')
    
    for word in words:
        word_list.append(word)
        
    word_list.sort()
    print(word_list)

command = int(input("""Enter the command number to be executed:
                        1. Add a word
                        2. Search a word
                        3. Change spelling of a word
                        4. Delete
                        5. See alphabetically list
                        """))
                        
if command == 1:
    add_word()
    
elif command == 2:
    search()
    
elif command == 3:
    change_spell()

elif command == 4:
    delete()
    
elif command == 5:
    sorted_list()

else:
    print("Incorrect Choice.")
                        

