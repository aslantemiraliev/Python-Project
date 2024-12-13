def is_valid_password (password):
    if len(password) < 6:
        return False
    if not password.isalnum():
        return False
    return True

password = input("Введите пароль:")
print(is_valid_password(password))



def the_nearest_date(List, target_number=0):
    closest_num = list[0]
    smallest_diff = abs(closest_num - target_number)
    for num in list:
              diff=abs(num-target_number)
        if diff < smallest_diff:
           closest_num = num
           smallest_diff = diff
    return closest_num
print(f'Ближайшее число: {the_nearest_date([1, 4, 10, 17, 22],12)}')