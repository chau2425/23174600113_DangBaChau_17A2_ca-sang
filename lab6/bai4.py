# a) Dãy Fibonacci
n = int(input("Nhập số lượng số Fibonacci cần tạo: "))

fibonacci_sequence = [0, 1]
for i in range(2, n):
  fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

print("Dãy Fibonacci", n, "số đầu tiên:", fibonacci_sequence)

# b) Danh sách số nguyên tố
prime_numbers = []
for num in range(2, 100):
  is_prime = True
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    prime_numbers.append(num)

print("Danh sách số nguyên tố nhỏ hơn 100:", prime_numbers)
