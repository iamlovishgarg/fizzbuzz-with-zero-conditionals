def fizzBuzz(n=1500):
    ans = []
    for i in range(1, n+1):
        divisible_by_3 = (i % 3 == 0)
        divisible_by_5 = (i % 5 == 0)
        
        if divisible_by_3 and divisible_by_5:
            ans.append("FizzBuzz")
            continue
        elif divisible_by_3:
            ans.append("Fizz")
        elif divisible_by_5:
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans


def fizzBuzzFast(n=1500):
    ans = []

    d = {
        0: "FizzBuzz",
        3: "Fizz",
        6: "Fizz",
        9: "Fizz",
        12: "Fizz",
        5: "Buzz",
        10: "Buzz",
    }
    
    for i in range(1, n+1):
        by_15 = i%15
        ans.append(d.get(by_15, str(i)))
        
    return ans

def fizzBuzzWithOneCondition(n=1500):
    ans = []

    d = {
        0: "FizzBuzz",
        3: "Fizz",
        6: "Fizz",
        9: "Fizz",
        12: "Fizz",
        5: "Buzz",
        10: "Buzz",
    }

    keys = d.keys()
    
    for i in range(1, n+1):
        by_15 = i%15
        if by_15 in keys:
            ans.append(d[by_15])
        else:
            ans.append(str(i))
        
    return ans

def worstOne(n=1500): # because of try catch
    ans = []

    d = {
        0: "FizzBuzz",
        3: "Fizz",
        6: "Fizz",
        9: "Fizz",
        12: "Fizz",
        5: "Buzz",
        10: "Buzz",
    }
    
    for i in range(1, n+1):
        by_15 = i%15
        try:
            ans.append(d[by_15])
        except:
            ans.append(str(i))
        
    return ans

if __name__=="__main__":
    n = 150000

    first = fizzBuzz(n)
    second = fizzBuzzFast(n)
    third = fizzBuzzWithOneCondition(n)
    fourth = worstOne(n)

    print(first==second==third==fourth)