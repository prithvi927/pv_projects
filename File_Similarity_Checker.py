

import re    # re module imported. this gives you the power of regular expressions, used to remove punctuation and normalize text.

def normalize(text):   #You're creating a function called normalize() with the parameter variable as text The main logic to create this function is that it will take any text and clean it up for comparison.
    text=text.lower()  # converts the content in the text variable to lower case and stores it in the same varaible "text" leading to updatation of the content in the text variable
    text=re.sub(r'[^\w\s]',' ',text)  # substitute anything that is not word and spaces with an empty string ('') i.e nothing.this again updates the content in the text variable 
    text=re.sub(r'\s+','',text) # substitute every group of multiple spaces /tabs/newlines with juat one single space('').this again updates the content in the text variable 
    text=text.strip()  # strip any exttra space from the staring and ending of the string (content in the the variable text). this again updates the content in the text variable 
    return text        # return the complete updated text


def file_matching(file1,file2): #creating a function file_matching with two parameter variables as file1 and file2
    with open(file1) as f1 ,open(file2) as f2 : # opening both the files (when user inouts file names as arguments) and closing them together and f1,f2 being the respective file object for each file
        data1=normalize(f1.read()) # normalize function is being called now with the content in the file no.1 (stored in file1 variable) read by "f1.read()" being the argument.
        data2=normalize(f2.read()) # again normalize function is being called now with the content in the file no.2 (stored in file2 variable) read by "f2.read()" being the argument.

    return (data1==data2) # data1 is equal to data2 ..true or false? the result is returned to the file_matching function

a=input("Enter file 1 name: ") # the file name input here (stored in the vriable a) is the argument to the parameter file1 in the file_matching function
b=input("Enter file 2 name: ") # the file name input here (stored in the vriable b) is the argument to the parameter file2 in the file_matching function

if file_matching(a,b): 
    print("❌ Possible scam: Content is highly identical.")
else:
    print("✅ No possible scam: Content is highly different.")


    
'''
 IMPORTANT NOTES ON WORKING OF SPECIFIC CODES: 

 re.sub(r'[^\w\s]','',text) in this line :
                              re.sub means substitute(sub) the regular expression pattern [^\w\s] with '' in the content in the text variable

                              
🔎 What does r'[^\w\s]' mean?

| Element        | Meaning                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------- |
| `r''`          | A **raw string** — it tells Python to treat backslashes `\` as literal                                              |
| `[ ]`          | A **character set** — match any single character **inside** the brackets                                            |
| `^`            | Inside `[ ]`, this means **"not"**                                                                                  |
| `\w`           | Matches any **word character** → letters (a-z, A-Z), digits (0-9), or underscore `_`                                |
| `\s`           | Matches any **whitespace character** → space, tab, newline, etc.                                                    |
| So `[^ \w \s]` | Means: **match anything that's NOT a letter, digit, underscore, or space** → basically, **punctuation and symbols** |

✅ Final meaning:
“Replace every character that's not a letter, number, underscore, or space with nothing (i.e., remove it).”

🛑 Example of the Scam It Catches:
👤 Person A wrote:

Machine learning is powerful. It helps automate tasks!
🕵️ Person B copied it, but changed punctuation:

Machine learning is powerful - it helps automate tasks??
👀 Looks different to the eye.

But after applying re.sub(r'[^\w\s]', '', text):

machilearningispowerfulithelpsautomatetasks
✅ Your program detects: ❌ Identical content




re.sub(r'\s+','',text) in this line:

                        re.sub means substitute(sub) the regular expression pattern \s+ with '' in the content in the text variable

                        
🔎 What does r'\s+' mean?

| Element  | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| `\s`     | Matches **any whitespace** → space, tab, newline, etc.       |
| `+`      | Means "**one or more**" of the thing before it               |
| So `\s+` | Means: **a group of 1 or more spaces, tabs, or line breaks** |

✅ Final meaning:
“Replace every group of multiple spaces/tabs/newlines with nothing '' ”


data1=normalize(f1.read()) In this line:

normalize function is called
f1.read reads the file content from the user input file name, also the read content by f1.read behaves as argument to the parameter text in the normalize function
all the text updatation takes place as normalize functions work is to update text and return the updataed text to the one who called the function
here, data1 variable called the function, so updated text is returned to the data1 variable 

similarly for this line data2=normalize(f2.read())


'''
