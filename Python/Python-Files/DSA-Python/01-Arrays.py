'''
Arrays In Data Sttructure
24 + 16 = 40 Hours
Data Types: int , string , boolean , float
No of Bytes : Data stored is == 4 bytes
1 int = 4 bytes
bytes will convert to bits
bits will conevrt to binary numbers
binary numbers = 0s,1s

arr[60] =


Built in Data Structures:

List:
  Mentioned []
  Separated commas,
  can contain duplicates,
  Ordered
  List are mutable
  List can be nested
  List are dynamic


Tuple :
  Parenthesis ()
  separated commas,
  Cannot contain duplicates
  Not Indexed
  Immutable
  Can be nested

Set:
  { } 
  Set are mutable can have multiple values


Dictionary:
  { } key Value pairs
  Whole dictionaries are mutable
  Keys Must me immutable
  Values can be either mutable or Immutable
  dictionaries are unordered
  Dictionaries can be accessed using keys


User Defined Data Structures

Stack
Queue
Linked List
Tree
Graph


'''

list1 = []
for i in range(0,10):
  list1[i] = list1.insert(i,int(input("number ")))

print(list1,end=" ")