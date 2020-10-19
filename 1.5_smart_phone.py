# cook your dish here
num = int(input())
budget = []
max_sales = 0
for _ in range(num):
    temp = int(input())
    budget.append(temp)
    

budget.sort(reverse=True)

for i in range(1,num+1):
    max_sales = max(max_sales, budget[i-1]*i)

print(max_sales)
