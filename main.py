# 6. Tub sonni aniqlash
n = int(input())
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))
print(is_prime)

# 7. Fibonacci (n ta)
n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b

# 8. Ro‘yxatdagi eng kichik son
lst = list(map(int, input().split()))
print(min(lst))

# 9. So‘z palindrommi?
s = input()
print(s == s[::-1])

# 10. Kvadratlar ro‘yxati
n = int(input())
print([i*i for i in range(1, n+1)])
