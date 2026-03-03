

def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    # return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))