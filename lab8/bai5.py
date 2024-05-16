def sum_divisors(n):
  divisors = [1]
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      divisors.append(n // i)
  return sum(divisors)

def is_amicable(num1, num2):
  if num1 == num2:
    return False
  return sum_divisors(num1) == num2 and sum_divisors(num2) == num1

num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

if is_amicable(num1, num2):
  print(f"{num1} và {num2} là hai số amicable.")
else:
  print(f"{num1} và {num2} không phải là hai số amicable.")
