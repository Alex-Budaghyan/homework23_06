def merge(ls1, ls2):
    i = 0
    j = 0
    merge_array = []
    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            merge_array.append(ls1[i])
            i += 1
        else:
            merge_array.append(ls2[j])
            j += 1
    while i < len(ls1):
        merge_array.append(ls1[i])
        i += 1
    while j < len(ls2):
        merge_array.append(ls2[j])
        j += 1
    return merge_array


def int_str(num):
    if num > 1015:
        print("Enter number between 1 to 1015: ")
    if num == 0:
        return "zero"
    number_dict1 = {
        '0': "", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
        '7': "seven", '8': "eight", '9': "nine"
    }
    number_dict2 = {
        '11': "eleven", '12': "twelve", '13': "thirteen", '14': "fourteen",
        '15': "fifteen", '16': "sixteen", '17': "seventeen", '18': "eighteen",
        '19': "nineteen"
    }
    number_dict3 = {
        '0': "", '1': "ten", '2': "twenty", '3': "thirty", '4': "forty", '5': "fifty", '6': "sixty",
        '7': "seventy", '8': "eighty", '9': "ninety"
    }
    number_dict4 = {
        '0': "", '1': "one hundred", '2': "two hundred", '3': "three hundred", '4': "four hundred",
        '5': "five hundred", '6': "six hundred", '7': "seven hundred", '8': "eight hundred",
        '9': "nine hundred"

    }
    num = str(num)
    if len(num) == 1:
        return number_dict1[num[0]]
    elif 11 <= int(num) <= 19:
        return number_dict2[num]
    elif len(num) == 2:
        return number_dict3[num[0]] + ' ' + number_dict1[num[1]]
    elif len(num) == 3:
        if 11 <= int(num) % 100 <= 19:
            return number_dict4[num[0]] + ' ' + number_dict2[str(int(num) % 100)]
        else:
            return number_dict4[num[0]] + ' ' + number_dict3[num[1]] + ' ' + number_dict1[num[2]]
    elif int(num) >= 1000:
        return 'a thousand ' + number_dict4[num[1]] + ' ' + number_dict3[num[2]] \
            + ' ' + number_dict1[num[3]]


def is_sorted(list1):
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            return False
    return True


def calculate_area(radius):
    return 3.14 * radius ** 2


counter = 0
def increment_counter():
    global counter
    counter += 1
    print(counter)


def outer_function(x):
    def inner_function(factor):
        return factor * x
    result = inner_function(4)


x = 10
def my_function():
    x = 20
    print("Local x: ", x)
    print("Global x: ", globals()["x"])


def power_of(n):
    def power(x):
        return x ** n
    return power


ls1 = [2, 4, 6, 8]
ls2 = [1, 3, 5, 7, 9]
print(merge(ls1, ls2))
print(int_str(156))
print(is_sorted(ls1))
print(calculate_area(5))
increment_counter()
increment_counter()
increment_counter()
increment_counter()
outer_function(18)
my_function()
k = power_of(8)
print(k(3))
