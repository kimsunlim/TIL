#백준 1037 약수



N = int(input())
A = list(map(int, input().split()))

#진짜 약수가 모두 주어지기 때문에
#가장 작은값과 가장 큰값을 곱하면
#진짜 수를 구할수 있다

max=max(A)
min=min(A)

print(max*min)