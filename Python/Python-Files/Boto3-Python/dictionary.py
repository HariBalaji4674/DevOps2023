myDict = {"name":"Peddireddy", "age":23,"Section" : "abc"}
myDict2 = {"skill1":"Linux","skill2":"Shell-Script","skill3":"Docker"}
print(myDict['name'])

myDict['course'] = "DevOps"
myDict['Duration'] = "3 Months"
myDict['Skills'] = myDict2

print(myDict["Skills"]["skill1"])

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])