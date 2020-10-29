
n = int(input())
summary = 0
while n > 0:
    calculation = n % 10
    summary = summary + calculation
    n = n // 10
print(summary)




