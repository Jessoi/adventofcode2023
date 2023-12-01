data = open('day_01.txt', 'r').read().split('\n')
print(data)

NUM_STRINGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_first_num(string):
    cur_str = ''
    for c in string:
        if c.isdigit():
            return c
        cur_str += c
        for i, strnum in enumerate(NUM_STRINGS):
            if strnum in cur_str:
                return str(i + 1)
    return '0'

def find_last_num(string):
    cur_str = ''
    for c in string[::-1]:
        if c.isdigit():
            return c
        cur_str = c + cur_str
        for i, strnum in enumerate(NUM_STRINGS):
            if strnum in cur_str:
                return str(i + 1)
    return '0'

def decode(data):
    res = []
    for string in data:
        res.append(int(find_first_num(string)+find_last_num(string)))
    return sum(res)


print(decode(data))