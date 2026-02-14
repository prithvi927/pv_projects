

import re

words_to_be_censored=[]

while True:
    try:
        n=int(input("Enter number of words to be censored: "))
        break
    except ValueError:
        print("Invalid entry!!!\nTry again ")

for i in range(n):
    words_to_be_censored.append(input(f"Enter the word to be censored {i+1}: "))
    
    
    
print(words_to_be_censored)


with open("list_of_words.txt","r+") as f:
    data=f.read()
    
    for word in words_to_be_censored:
        pattern=re.compile(rf"(?i)\b{re.escape(word)}\b")
        data=pattern.sub("#"*len(word),data)

    f.seek(0)
    f.truncate()
    f.write(data)

    

'''Working: 

import re :  Regex module imported

words_to_be_censored=[]:  an empty list is made where the "to be censored words will be appended 

while True: this is how we start an infinite loop  by hardcoding the the condition of the while loop as 'True' itself since the condition 
            itself is true so the loop cannot break until "break" is applied

try:
        n=int(input("Enter number of words to be censored: "))
        break
    except ValueError:
        print("Invalid entry!!!\nTry again ")


        this is the try-except block: 

        💡 What try-except does:
            The try block says:

            “Try to run this code — and if it throws an error (like ValueError), then don't crash. Handle it gracefully.”

            
            🔍 How it works here :
                            try: tries to convert the input to an integer.

                            break:breaks the loop if input converted to an integer succesfully

                            If it fails (e.g., input was "hello" or "5.6"), it raises a ValueError.

                            except ValueError:  catches that error and prints a message.

                            Because you're inside a while True loop, the user can try again as many times as needed.

for i in range(n): a for loop has been set on a fix range from 0 to n , n is  the number of words to be censored

words_to_be_censored.append(input(f"Enter the word to be censored {i+1}: ")): to be censored words (after entering) are appended to the list in each iteration

print(words_to_be_censored): list of to be cencored words are printed

with open("list_of_words.txt","r+") as f: file is opened in r+ (read and write) mode

data=f.read(): the program read the file and stored the read content in the data variable

for word in words_to_be_censored: a loop is created with the itertion of the words in the "words_to_be_cencored list"

 pattern=re.compile(rf"(?i)\b{re.escape(word)}\b"): 
 
                                                    It creates a regex pattern that is:

                                                    Case-insensitive ((?i))

                                                    Whole-word match only (\b... \b)

                                                    (re.escape(...)): special characters are also taken literally

this is like "pattern" is a person and we instructed him " see bro i would be u will get the word (to be censored) in each iteration, do not consider 
its case, strictly take the whole word and also the special characters literally okay"

 data=pattern.sub("#"*len(word),data): now after instructing the person "pattern" we instructed him "bro theres this data veriable where the read
 content of the file is stored, take the word (to be censored) u got in each iteration...match the whole word with the words in the read content stored in the data 
 variable and substitute the matched words with "#" times the lenght of the substituted word...in the data variable itself and continue substituting the
 matched words in each iteration in the data variable itself

 NOTE : there should not be the use of two different variables...i.e one variable for storing the read content and a different variable for storing
 the content with the censored (substituted) words...as the other variable will not store the previous censorship done in the previous iteration 
 till the last censorship  eg: data=f.read() but new_data=pattern.sub("#"*len(word),data) this should be avoided this will work when a single word is being
 censored but not when a group of word will get censored 

 
 f.seek(0): file pointer reaches at the begining of the file as after reading pointer was at the end of the file 

 f.truncate(): this clears the previous content in the file starting from the current pointer position so b4 using truncate, using seek(0) is necessary so that 
 pointer is at the starting and truncte clears the file from the starting 

 f.write(data): this writes the  updated censored content in the file
 NOTE= in r+ mode write doesnt clears the file as it does in w or w+ mode so we hv to first manually truncate the file and then write the new updated censored content
 or else it will  write on the previous content itself
  


'''
                
    












