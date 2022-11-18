# Question 1
# 5
# 0
# 5
# 5


# Question 2
def foo_looper(n):
    while n <= 10:
        if n == 1:
            print("1st loop")
        elif n == 2:
            print("2nd loop")
        elif n == 3:
            print("3rd loop")
        elif n > 0:
            print(f"{n}th loop")
        
        if n == 9:
            print("second to last loop")
        
        n += 1


# Question 3
def loop_printer(n):
    for i in range(n, 0, -1):
        print(i)


# Question 4
def foo_bounded_while(start, end):
    print(start)
    while True:
        start **= 2
        print(start)
        if start > end:
            break

