#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd

# In[5]:


import regex as re


# In[15]:


text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))


# In[17]:


data = {'Summary' : ['hello word!', 'XXXXX text', '123four, five:; six...']}
df= pd.DataFrame(data)
df['SUMMARY'] = df['Summary'].str.replace('[^a-zA-Z\s]', '', regex=True)
print(df)


# In[23]:


import regex as re


# In[25]:


text = 'Lilly noticed that the pretty doll was dressed very elegantly.'
print(re.findall(r"\b\w{4,}\b", text))


# In[192]:


#Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

import re

def find_words(string):
  pattern = re.compile(r'\b\w{3,5}\b')
  matches = pattern.findall(string)
  return matches

string = "This is a sample string with words off different lengths."
result = find_words(string)
print(result)


# In[194]:


#Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
import re

def find_words(string):
  pattern = re.compile(r'\b\w{4}\b')
  matches = pattern.findall(string)
  return matches

string = "This is a sample string with words off different lengths."
result = find_words(string)
print(result)


# In[41]:


#Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.


import re 
texts = ["example(.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
for text in texts:
    print(re.sub(r" ?\([^)]+\)", "", text))


# In[ ]:





# In[45]:


#Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]

import re
text = 'ImportanceOfRegularExpressionsInPython'
result = re.findall('[A-Z][^A-Z]*', text)

print(result)


# In[67]:


#Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re
def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces('RegularExpression1IsAn2ImportantTopic3InPython'))


# In[85]:


#Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

import re
def insert_spaces(text):
    return re.sub(r'\b(?=[A-Z 0-9])', ' ', text)

text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces(text)
print(result)  


# In[199]:


import re

def insert_spaces(text):
  # Use regular expression to find words starting with capital letters or numbers
  pattern = r'([A-Z][a-z0-9]+|\d+)'
  # Replace the matched words with a space followed by the word
  result = re.sub(pattern, r' \1', text)
  # Remove any leading or trailing spaces
  result = result.strip()
  return result


# In[201]:


import pandas as pd
import numpy as np
import regex as re

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)


# In[203]:


df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])


# In[105]:


#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
import re
def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return('Not matched!')

print(text_match("Lilly noticed that the pretty doll was dressed very elegantly."))
print(text_match("Python_Exercises_1"))


# In[117]:


#Write a Python program where a string will start with a specific number. 

import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False

print(match_num('5-25689445'))
print(match_num('7-23456789'))


# In[119]:


#Write a Python program to remove leading zeros from an IP address

import re
ip = "216.09.084.186"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[136]:


#Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.

import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b([A-Z][a-z]+) \d{1,2}(?:st|nd|rd|th)? \d{4}\b"

matches = re.findall(pattern, text)
print(matches)


# In[140]:


#Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

import re
my_string = 'The quick brown fox jumps over the lazy dog.'
m = re.search('dog|fox|horse', my_string)
if m:
    print('it\'s a match')
else:
    print('no match found')


# In[142]:


#Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'

import re

pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % (match.re.pattern, match.string, s, e))


# In[205]:


#Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


# In[146]:


text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[148]:


#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
    
import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[150]:


#Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
#Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
#Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']

import re

def find_decimal_numbers(string):
  pattern = re.compile(r'\d+\.\d{1,2}')
  decimal_numbers = re.findall(pattern, string)
  return decimal_numbers

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print(output)


# In[152]:


#Write a Python program to separate and print the numbers and their position of a given string.

import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[156]:


#Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950

import re

# Extract all numeric values from the string.
occ = re.findall("\d+", "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642")

# Convert the numeric values from string to int.
num_list = map(int, occ)

# Find and print the max
print(max(num_list))


# In[158]:


#Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python

import re

def insert_spaces(text):
  # Use regular expression to find words starting with capital letters
  pattern = r'([A-Z][a-z]+)'
  # Replace the found words with the same word followed by a space
  result = re.sub(pattern, r' \1', text)
  # Remove any leading or trailing spaces
  result = result.strip()
  return result

sample_text = "RegularExpressionIsAnImportantTopicInPython"
output = insert_spaces(sample_text)
print(output)


# In[160]:


#Python regex to find sequences of one upper case letter followed by lower case letters 

import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))


# In[162]:


#Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world

import re

def remove_duplicates(sentence):
  pattern = r'\b(\w+)(\s+\1\b)+'
  return re.sub(pattern, r'\1', sentence)

# Example usage
sentence = "Hello hello world world"
result = remove_duplicates(sentence)
print(result)


# In[164]:


#Write a python program using RegEx to accept string ending with alphanumeric character.

import re
text1 = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))


# In[166]:


#Write a python program using RegEx to accept string ending with alphanumeric character.

import re

regex_expression = '[a-zA-z0-9]$'

def check_string(my_string):

   if(re.search(regex_expression, my_string)):
      print("The string ends with alphanumeric character")

   else:
      print("The string doesnot end with alphanumeric character")


my_string_1 = "Python@"
print("The string is :")
print(my_string_1)
check_string(my_string_1)

my_string_2 = "Python1245"
print("\nThe string is :")
print(my_string_2)
check_string(my_string_2)


# In[168]:


#Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']


import re

def extract_hashtags(text):
  hashtags = re.findall(r'#\w+', text)
  return hashtags

# Sample text
text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'

# Extract hashtags
hashtags = extract_hashtags(text)

# Print the extracted hashtags
print(hashtags)


# In[170]:


#Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders


import re

input_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern = r"<U\+\w{4}>"
output_text = re.sub(pattern, "", input_text)

print(output_text)


# In[184]:


#Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.


import re

def remove_words(string):
  pattern = re.compile(r'\b\w{2,4}\b')
  modified_string = re.sub(pattern, '', string)
  return modified_string

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
expected_output = "following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly."

result = remove_words(sample_text)
print(result == expected_output)


# In[ ]:





# In[ ]:




