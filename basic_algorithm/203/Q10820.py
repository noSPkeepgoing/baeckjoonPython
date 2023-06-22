while True:
    result = [0] * 4
    try:
        str = input()
        for s in str:
            if s.islower():
                result[0] += 1
            elif s.isupper():
                result[1] += 1
            elif s.isdigit():
                result[2] += 1
            else:
                result[3] += 1
        print(*result)
    except:
        break
