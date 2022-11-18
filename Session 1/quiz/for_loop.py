# Question 1
# 0
# 2
# 3.3
# test


# Question 2
def get_max(in_list):
    max = in_list[0]
    for item in in_list:
        if item > max:
            max = item
    return max


def get_min(in_list):
    min = in_list[0]
    for item in in_list:
        if item < min:
            min = item
    return min


def max_and_min_number_in_list(in_list):
    return get_max(in_list), get_min(in_list)


# Question 3
def average_list(in_list):
    return sum(in_list) / len(in_list)


# Question 4
def triangle_stars(n):
    for i in range(1, n * 2):
        line_number = min(i, n * 2 - i)
        for j in range(line_number):
            print("* ", end="")
        print(line_number)
