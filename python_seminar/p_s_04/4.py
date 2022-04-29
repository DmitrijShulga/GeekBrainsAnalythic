numbers_init = [1, 1, 100, 100, 25, 34]
numbers_result = []
for i in numbers_init:
    if i not in numbers_result:
        numbers_result.append(i)
print (numbers_result)