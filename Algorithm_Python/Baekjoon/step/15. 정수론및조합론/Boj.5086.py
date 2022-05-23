### 정수론 및 조합론

#백준 5086 배수와 약수



while True:
    n,m =map(int,input().split())
    if n==0 and m==0:
        break
    if m % n ==0: # 첫번째 숫자가 두번째 숫자의 약수일경우
        print('factor')
        
    elif n % m ==0: #첫번째숫자가 두번째 숫자의 배수일 경우
        
        print('multiple')
        
    else: 
       print ('neither')
