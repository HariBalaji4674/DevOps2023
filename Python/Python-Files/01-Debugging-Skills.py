def display():
  for i in range(1,11):
    if i == 10:
      print("Bye !!!")

display()

def Fibonacci(n):
  # for i in range(0,n):
  if n == 1:
    return 1
  else:
    return (n*Fibonacci(n-1))

fib = Fibonacci(10)
print(fib)