import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()

for _ in range(10):
    filename = random.choice(WORDS).decode('utf-8')
    with open(f'test_folder/{filename}.txt', 'w') as f:
        f.write(filename)