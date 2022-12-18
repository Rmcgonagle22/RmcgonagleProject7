def compound_interest(initial_balance, interest_rate,years_past):
    if years_past == 0:
        return init_bal
    if init_bal == 0:
        return 0

def reverseString(string):
    if len(Palindrome) <= 1:
        return Palindrome

    return Palindrome[-1] + reverseString(string[:-1])

def loop_fact(n):
    result = 1
    for number in range(1,n):
        result = result*number
    return n*result

def fact(n):
    if n<=1:
        return 1
    return  n * fact(n-1)

def main():
    my_n = int(input("what number shall we calculate factorial:"))
    result = fact(my_n)
    print(f"the result is {result}")

main()

def main():
    student_data = get_data("students.txt")
    student_data.sort(key=get_key)
    stu_to_find = input("what student should we find")
    result = binary_search(student_data, stu_to_find)
    print(result)
#    for stu in student_data:
#        print(stu)

def draw_triangle(length):
    pen.setheading(180)      # set the direction of the pen to left
    for i in range(3):       # draw 3 sides
        pen.rt(120)          # rotate the pen 120 degrees clockwise
        pen.fd(length)

import arcade #type: ignore
def ClassArcade():
    win = Window.Window(500, 500)
    win.load()
    arcade.run()
#this part below is not correct and I will correct it shortly
def draw_triangle(length):
    pen.setheading(180)      # set the direction of the pen to left
    for i in range(3):       # draw 3 sides
        pen.rt(120)          # rotate the pen 120 degrees clockwise
        pen.fd(length)       # draw side
                             # pen will end facing left (180)