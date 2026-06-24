full_dot = '●'
empty_dot = '○'
def create_character(name, my_str, my_int, my_char):
    if not isinstance (name, str):
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    if not isinstance(my_str, int):
        return 'All stats should be integers'
    if not isinstance(my_int, int):
        return 'All stats should be integers'
    if not isinstance(my_char, int):
        return 'All stats should be integers'
    if my_str < 1 or my_int < 1 or my_char < 1:
        return 'All stats should be no less than 1'
    if my_str > 4  or my_int > 4 or my_char > 4:
        return 'All stats should be no more than 4'
    if my_str + my_int + my_char != 7:
        return 'The character should start with 7 points'
    return f'{name}\nSTR {full_dot * my_str}{empty_dot * (10 - my_str)}\nINT {full_dot * my_int}{empty_dot * (10 - my_int)}\nCHA {full_dot * my_char}{empty_dot * (10 - my_char)}'