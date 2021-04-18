def sum_in_list(array, number):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                if array[i] + array[j] == number:
                    return True 
    return False 
with open(r'F:\Own_Projects\Challenges\Day_Nine\output.txt') as output:
    preamble = 25
    count = 0
    valid_numbers = []
    array_part_2 = []
    for i in output.readlines():
        array_part_2.append(int(i))
        if count < preamble:
            valid_numbers.append(int(i))
        else:
           if sum_in_list(valid_numbers, int(i)):
                valid_numbers.pop(0)
                valid_numbers.append(int(i))
           else:
                answer = int(i)
                print('The number that does not follow the rule is:', answer)
                break
        count += 1


# part Two


upper_limit = len(array_part_2) - 1
flag = 0
while(flag == 0):
    accumulator = 0
    set_elements = []
    for i in reversed(array_part_2[:upper_limit]):
        accumulator += i
        set_elements.append(i)
        if accumulator == answer:
            answer_part_2 = max(set_elements) + min(set_elements)
            flag = 1
            break
        if accumulator > answer:
            upper_limit -= 1
            break
print('the answer for the part two is:', answer_part_2)    