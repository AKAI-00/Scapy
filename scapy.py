import requests
from bs4 import BeautifulSoup
import re

url = input("Please enter the website url : ")
min_length = int(input("Enter the minimum length for words: "))
max_length = int(input("Enter the maximum lenth for words: "))

output_file = input("Enter the name for the output file: ")

response = requests.get(url)
if response.status_code != 200:
    print("error fetching th url")
    exit

soup = BeautifulSoup(response.content,'html.parser')
text=soup.get_text()
words = re.findall(r'\b\w+\b',text)
filtered_words = [word for word in words if min_length <=len(word)<=max_length]

with open(output_file,'w')as file:
    for word in filtered_words:
        file.write(word +'\n')

