import json
people = '''
{
      "rollnos" :[22,34,45,67,87],
      "idea" : [{
        "Person1" : {
          "name" : "Albert-einstien",
          "age" : 60,
          "city" : "London",
          "email" : "albert@gmail.com"
        },
        "Person2" : {
          "name" : "Albert-Robert",
          "age" : 45,
          "city" : "London",
          "email" : "albert123@gmail.com"
        },
        "Person3" : {
          "name" : "Albert-marskov",
          "age" : 89,
          "city" : "London",
          "email" : "albert000@gmail.com"
        }
     } ],
      "person": {
                  "name": "John Doe",
                  "age": 30,
                  "city": "New York",
                  "email": "john@example.com"
                },
      "book": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "published_year": 1925,
                "genre": "Fiction"
              },
      "movie": {
                  "title": "Inception",
                  "director": "Christopher Nolan",
                  "release_year": 2010,
                  "genre": "Science Fiction"
                }
}
'''
data  = json.loads(people)
print(type(data))

print(data['rollnos'][0])
print(data['person']['name'])

print(data['idea'][0]['Person1'])

# print(data['peoples'])
# for i in data['peoples']:
#   print(i["peoples"]["person"])