#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import re

text = 'Python Exercises, PHP Exercises.'
print(re.sub("[ ,.]", ":" , text))


# In[2]:


import pandas as pd
import numpy as np
import re

data = {'SUMMARY' :['hello, world!','XXXXXtest', '123four, five:; six...']}

df = pd.DataFrame(data)

df['SUMMARY'] = df['SUMMARY'].str.replace('[^a-zA-Z\s]', '', regex=True)
                                          
print(df)


# In[3]:


import re 

def find_long_words(string):

    pattern = re.compile(r'\b\w{4}\b')
    long_words = pattern.findall(string)
    return long_words

string = "This is a sample string with words of different lengths."
result = find_long_words(string)
print(result)


# In[4]:


import re

def find_words(string):
  pattern = re.compile(r'\b\w{3,5}\b')
  matches = pattern.findall(string)
  return matches

string = "This is a sample string with words o f different lengths."
result = find_words(string)
print(result)


# In[5]:


import re

def remove_parentheses(strings):
    #compile a regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\s*\(*?\)')
    
    #Iterate through the list of strings and apply the regular expression pattern
    result = []
    for s in strings:
        #Replace the matched pattern with an empty string
        new_s = pattern.sub('', s)
        result.append(new_s.strip())
        
    return result

sample_text = ["example(.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

output = remove_parentheses(sample_text)
print('\n'.join(output))


# In[6]:


import re

#Write the sample text to a text file.
sample_text = ['example (.com)', "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
with open('sample.txt', 'w') as file:
    for line in sample_text:
        file.write(f'{line}\n')

#Read the content of the text file.
with open('sample.txt', 'r') as file:
    content = file.read()

#Use Regular Expression (regex) to remove the parenthesis area.
cleaned_content = re.sub(r'\s*\(.*?\)\s*', '', content)

#Print the result.
print(cleaned_content.strip().split('\n'))


# In[7]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"

#Define the regular expression pattern to match uppercase letters
pattern = r"(?<=[a-z])(?=[A-Z])"

#Split the string using the regular expression pattern 
split_string = re.split(pattern, sample_text)

#Print the split string
print(split_string)


# In[8]:


import re 

def insert_spaces_before_numbers(text):
    #Define the regular expression pattern to match words starting with a number
    pattern = r"(\d+\w*)"
    
    #Replace the matches with a space followed by the match 
    return re.sub(pattern, r" \1", text)

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces_before_numbers(sample_text)

print(result)


# In[9]:


import re 

def insert_spaces_before_numbers(text):
    #Define the regular expression pattern to match words starting with a number
    pattern = r"((?<=\s)[A-Z\d]|(?<!\A)[A-Z\d])"
    
    #Replace the matches with a space followed by the match 
    return re.sub(pattern, r" \1", text)

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
result = insert_spaces_before_numbers(sample_text)

print(result)


# In[10]:


import pandas as pd

# Read the data from the GitHub link
url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)

# Extract the first 6 letters of each country name and store it in a new column
df['first_five_letters'] = df['Country'].str[:6]

# Display the first few rows of the dataframe
print(df.head())


# In[11]:


import re

def match_string():
    pattern = r"^[a-zA-Z0-9_]*$"
    while True:
        user_input = input("Enter a string containing only upper and lowercase letters, numbers, and underscores: ")
        if re.match(pattern, user_input):
            print("The string matches the pattern!")
            break
        else:
            print("The string does not match the pattern. Please try again.")

# Run the function
match_string()


# In[12]:


import re

def match_string_starting_with_number():
    pattern = r"^123"
    while True:
        user_input = input("Enter a string starting with 123: ")
        if re.match(pattern, user_input):
            print("The string matches the pattern!")
            break
        else:
            print("The string does not match the pattern. Please try again.")

# Run the function
match_string_starting_with_number()


# In[13]:


def remove_leading_zeros(ip):
    # Split the IP address into its four octets
    octets = ip.split('.')
    
    # Remove leading zeros from each octet
    octets = [octet.lstrip('0') for octet in octets]
    
    # Join the octets back together into an IP address
    ip = '.'.join(octets)
    
    return ip

# Test the function with an example IP address with leading zeros
ip_with_leading_zeros = '192.168.001.020'
print(remove_leading_zeros(ip_with_leading_zeros))


# In[16]:


import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"(?i)\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(?:st|nd|rd|th)\s+\d{4}\b"

matches = re.findall(pattern, text)
print(matches)


# In[17]:


def search_words(text, words):
    """
    Searches for the given words in the text and returns a list of
    found words with their indices.

    :param text: The text to search in.
    :param words: A list of words to search for.
    :return: A list of tuples, where each tuple contains a word and its index.
    """
    found_words = []
    for word in words:
        if word in text:
            index = text.index(word)
            found_words.append((word, index))

    return found_words

# Sample text
text = 'The quick brown fox jumps over the lazy dog.'

# Searched words
words = ['fox', 'dog', 'horse']

# Search for the words
found_words = search_words(text, words)

# Print the results
for word, index in found_words:
    print(f'Found "{word}" at index {index}')


# In[18]:


import re

# Sample text
text = 'The quick brown fox jumps over the lazy dog.'

# Searched words
searched_word = 'fox'

# Search for the substring in the text
index = text.find(searched_word)

# Print the result
if index != -1:
    print(f'Found "{searched_word}" at position {index}')
else:
    print(f'Could not find "{searched_word}" in the text')


# In[19]:


import re

# Sample text
text = 'Python exercises, PHP exercises, C# exercises'

# Searched word
searched_word = 'exercises'

# Initialize the index to 0
index = 0

# Loop until the substring is not found
while True:
    # Search for the substring in the text
    index = text.find(searched_word, index)

    # If the substring is not found, break the loop
    if index == -1:
        break

    # Print the result
    print(f'Found "{searched_word}" at position {index}')

    # Increment the index to start the search from the next position
    index += len(searched_word)


# In[20]:


import re

def find_occurrences(string, substring):
    
    positions = []
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        positions.append(start)
        start += len(substring)

    return {
        'occurrences': len(positions),
        'positions': positions
    }

# Example usage:
string = "Hello, welcome to Python programming! Python is a great language."
substring = "Python"

result = find_occurrences(string, substring)
print(result)


# In[21]:


from datetime import datetime

def convert_date_format(date_str):
    # Parse the date string in the "yyyy-mm-dd" format
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # Format the date object as a string in the "dd-mm-yyyy" format
    formatted_date = date.strftime("%d-%m-%Y")

    return formatted_date

# Example usage
date_str = "2024-03-05"
formatted_date = convert_date_format(date_str)
print(formatted_date)


# In[22]:


import re

def find_decimal_numbers(text):
    pattern = r'\b\d+\.\d{1,2}\b'
    decimal_numbers = re.findall(pattern, text)
    return decimal_numbers

text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
decimal_numbers = find_decimal_numbers(text)
print(decimal_numbers)


# In[23]:


import re

def find_numbers(text):
    # Find all numbers in the text
    numbers = re.findall(r'\b\d+\.\d{1,2}\b|\b\d+\b', text)
    
    # Print the numbers and their positions
    for i, number in enumerate(numbers):
        start = text.index(number)
        end = start + len(number)
        print(f"Number: {number}, Position: {(start, end)}")

# Test the function with the sample text
text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
find_numbers(text)


# In[24]:


import re

def extract_max_num(text):
    # Find all the numeric values in the text using a regular expression
    nums = re.findall(r'\d+', text)
    
    # Convert the list of strings to integers
    nums = [int(num) for num in nums]
    
    # Return the maximum value
    return max(nums)

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
print(extract_max_num(sample_text))


# In[25]:


def insert_spaces(text):
    """Insert spaces before capitalized letters in a string."""
    # Use a regular expression to find capitalized letters and insert a space before them.
    return re.sub(r'([A-Z])', r' \1', text)

# Example usage
text = "RegularExpressionIsAnImportantTopicInPython"
print(insert_spaces(text))  # Regular Expression Is An Important Topic In Python


# In[26]:


import re

# Match one uppercase letter followed by one or more lowercase letters
pattern = r'[A-Z][a-z]+'

# Example string
text = "ThisIsAnExampleStringWithSomeCapitalizedWords"

# Find all matches
matches = re.findall(pattern, text)

# Print the matches
print(matches)  # ['This', 'Is', 'An', 'Example', 'String', 'With', 'Some', 'Capitalized', 'Words']


# In[28]:


import re

def remove_continuous_duplicate_words(sentence):
    
    # Use a regular expression pattern to match one or more word characters followed by a space
    pattern = r'\b(\w+)\s\1\b'

    # Use the re.sub() function to replace all occurrences of the pattern with the first word character group
    result = re.sub(pattern, r'\1', sentence)

    # Return the result
    return result

# Example usage
sample_text = "Hello hello world world"
print(remove_continuous_duplicate_words(sample_text))


# In[29]:


import re

def ends_with_alphanumeric(string):
    """
    Check if a string ends with an alphanumeric character using regular expression.

    :param string: str, the input string
    :return: bool, True if the string ends with an alphanumeric character, False otherwise
    """
    # Use a regular expression pattern to match one or more alphanumeric characters at the end of the string
    pattern = r'\w+$'

    # Use the re.search() function to check if the pattern matches the input string
    match = re.search(pattern, string)

    # Return True if a match is found, False otherwise
    return bool(match)

# Example usage
print(ends_with_alphanumeric("hello123"))  # Output: True
print(ends_with_alphanumeric("hello!"))  # Output: False


# In[30]:


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


# In[31]:


import re

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

# Regular expression pattern to match <U+..> like symbols
pattern = r"<U\+[0-9A-Fa-f]{4}>|<ed>"

# Remove the matched symbols using re.sub()
cleaned_text = re.sub(pattern, "", sample_text)

print(cleaned_text)


# In[32]:


import pandas as pd
import numpy as np
import re

text_file = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
def extract_dates(text_file):
    with open(text_file, 'r') as f:
        text = f.read()
        dates = parse(text, fuzzy_with_tokens=True)
        return [date[0] for date in dates if date[1]]

text_file = 'sample_text.txt'
print(extract_dates(text_file))


# In[33]:


import pandas as pd
import numpy as np
import re

text_file = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999."
def extract_dates(text_file):
    with open(text_file, 'r') as f:
        text = f.read()
        dates = parse(text, fuzzy_with_tokens=True)
        return [date[0] for date in dates if date[1]]

text_file = 'sample_text.txt'
print(extract_dates(text_file))


# In[34]:


import re

def remove_words(text):
    # Compile a regular expression pattern that matches words of length between 2 and 4
    pattern = re.compile(r'\b\w{2,4}\b')
    
    # Use the sub() method of the compiled pattern to replace all matching words with an empty string
    result = pattern.sub('', text)
    
    return result

text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

result = remove_words(text)

print(result)


# In[ ]:




