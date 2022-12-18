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

