#calculate factorial of 10

start = 10
ans = 1
i = 1

while i <= start:
  ans = ans * i
  i = i + 1

  print(ans, "factorial of", i-1)