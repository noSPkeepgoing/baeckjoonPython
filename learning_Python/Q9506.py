while 1 :
    n = int(input())

    if n == -1 :
        break
    else :
        nums = [i for i in range(1, n) if n % i == 0]
        
        if n == sum(nums) :
            print(n, '=', ' + '.join(str(n) for n in nums))
        else :
            print(n, 'is NOT perfect.')
