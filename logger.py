import os
from datetime import datetime
from functools import wraps


def logger(old_function):
# декоратор 1    
    path ='main.log'
    def new_function(*args, **kwargs):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name_function = old_function.__name__
        result = old_function(*args, **kwargs)
        result_log = f'{current_time}, {name_function}, {args}, {kwargs}, {result}\n'
        with open(path, 'a', encoding='utf-8') as file:
            file.write(result_log)
        return result
    return new_function

def logger_2(path):
# декоратор 2
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            name_function = old_function.__name__
            result = old_function(*args, **kwargs)
            result_log = f'{current_time}, {name_function}, {args}, {kwargs}, {result}\n'
            with open(path, 'a', encoding='utf-8') as file:
                file.write(result_log)
            return result
        return new_function
    return __logger    