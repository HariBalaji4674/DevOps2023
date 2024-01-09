'''
Give me The squares of Problems

'''

import json
import random


squares = [ x ** 2 for x in range(10)]
print(squares)

random_number = random.randint(1,100)
print(random_number)

random_numbers = []
for _ in range(10):
  random_number = random.randint(1,100)
  random_numbers.append(random_number)

print(random_numbers)

# Taking only even Number for randomly generated numbers

random_numbers = []
for _ in range(10):
  random_number = random.randrange(0,100,2)
  if random_number % 2 == 0:
    random_numbers.append(random_number)

print(random_numbers)


data = {'name':"peddireddy",'age':'20','year':'2000'}
json_string = json.dumps(data)
print(json_string)

from github import Github

access_token = "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"
g = Github(access_token)
user = g.get_user()
print("Repositories of the authenticated user ")
for repo in user.get_repos():
  print(repo.name)