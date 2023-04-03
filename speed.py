import timeit
import main

print("fizzBuzz:", timeit.timeit(main.fizzBuzz, number=10000)) # slow
print("fizzBuzzWithOneCondition:", timeit.timeit(main.fizzBuzzWithOneCondition, number=10000)) # blazingly fast
print("fizzBuzzFast:", timeit.timeit(main.fizzBuzzFast, number=10000)) # fast
print("worstOne:", timeit.timeit(main.worstOne, number=10000)) # slowest