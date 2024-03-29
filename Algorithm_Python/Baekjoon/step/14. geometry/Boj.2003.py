

#백준 2003 수열의 합

#투포인터: 1차원 배열에서 두개의 포인터를 조작하여 원하는 결과 얻는 알고리즘
#구간의 합 < Target(M) : 오른쪽 포인터 → 이동 / 합을 늘리기 위함
#구간의 합 > Target(M) : 왼쪽 포인터 → 이동 / 합계 줄이기 위함
#구간의 합 = Target(M) : 카운트 증가,  오른쪽 포인터 → 이동

N, M = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right<=N and left<=right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)

    if total == M:
        cnt += 1

        right += 1

    elif total < M:
        right += 1

    else:
        left += 1

print(cnt)
