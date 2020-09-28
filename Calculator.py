Input = input("Enter Operation: ")
Input = Input.replace(" ", "")

# use tupels with character and index of string
numbers = []
operator = []
operators = ['+','*','-','/']
# brackets = []

# Invalid Operation:
def is_number(n):
    try:
        float(n)  # Type-casting the string to `float`.
        # If string is not a valid `float`,
        # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

def Substring(index, index_end):
    #j = i
    print("j:")

    for j in Input[index:]:
        print(j)
        if j in operators:
            break
        else:
            #print("test2")
            index_end+=1
    return index_end



index = 0
index_end = index
substring = ''

for i in Input:
    #creates substring to the next operator
    print("index:")
    print(index)
    print("index_end")
    print(index_end)

    index_end = index

    index_end = Substring(index, index_end)
    print("index_end neu:")
    print(index_end)
    substring = Input[index:index_end]
    print(substring)

    #sorting operation for operators and numbers
    if is_number(substring):  # check if str 'Input' at index i is a number
        numbers.append((substring, index))
        subtring = ''
        index = index_end
        print("number:")
    elif i in operators:  # check if i is operator
        print("operator:")
        operator.append((i, index))
        index += 1
    else:
        print("Invalid Operation")
        break
################
# Punkt vor Strich


Result = Input

print(numbers)
print(operator)
print(Result)
