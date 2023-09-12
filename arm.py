def is_arm(number):
    st_num=str(number)
    no_digit=len(st_num)

    sum_num=sum(int(digit)**no_digit for digit in st_num)

    if sum_num==number:
        return True
    return False
n=int(input("eneter the number : "))
if is_arm:
    print("it is a arm strong number")
else:
    print("it is not an arm strong number..")
    