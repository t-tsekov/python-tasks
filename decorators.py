import string
import datetime
import time


def accepts(*types):
    def inner_accepts(func):
        def wrapper(*args, **kwargs):
            if len(types) != len(args):
                raise TypeError("{func_name} called with wrong number of arguments"
                                .format(func_name = func.__name__,))

            for i, (arg, typ) in enumerate(zip(args, types)):
                if not isinstance(arg, typ):
                    raise TypeError("Argument {arg_num} of {func_name} is not {typ}!"
                                    .format(arg_num = i+1, func_name = func.__name__, typ = typ))
            return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        return wrapper
    return inner_accepts


def encrypt(num):
    def inner_encrypt(func):
        def caesar(text):
            shift = num % 26

            alphabet_lower = string.ascii_lowercase
            alphabet_upper = string.ascii_uppercase

            shifted_alphabet_lower = alphabet_lower[shift:] + alphabet_lower[:shift]
            shifted_alphabet_upper = alphabet_upper[shift:] + alphabet_upper[:shift]

            alphabet = alphabet_lower + alphabet_upper
            shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper
            table = str.maketrans(alphabet, shifted_alphabet)

            return text.translate(table)

        def wrapper():
            text = func()
            return caesar(text)

        # this is done so that logging encrypted function calls would correctly display the function name
        wrapper.__name__ = func.__name__
        return wrapper
    return inner_encrypt


def log(filename):
    def inner_log(func):
        def wrapper(*args, **kwargs):
            try:
                with open(filename, mode = 'a') as file:
                    file.write('\n{func_name} was called at {date}'
                               .format(func_name = func.__name__, date = datetime.datetime.now()))
            except IOError as e:
                print(e)
            return func(*args, **kwargs)
        return wrapper
    return inner_log


def performance(filename):
    def inner_performance(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            execution_time = end - start

            try:
                with open(filename, mode = 'a') as file:
                    file.write('\n{func_name} was called and took {time} seconds to complete'
                               .format(func_name = func.__name__, time = execution_time))
            except IOError as e:
                print(e)

            return result
        return wrapper
    return inner_performance

# running the suggested examples
if __name__ == "__main__":
    print("First task:\n")

    @accepts(str)
    def say_hello(name):
        return "Hello, I am {}".format(name)

    print(say_hello("Hacker"))

    @accepts(str, int)
    def deposit(name, money):
        print("{} sends {} $!".format(name, money))
        return True

    deposit("RadoRado", 10)

    @accepts(str)
    def say_hello(name):
        return "Hello, I am {}".format(name)

    try:
        say_hello(4)
    except TypeError as err:
        print(err)

    print("-------------------------------\nSecond task:\n")

    @encrypt(2)
    def get_low():
        return "Get get get low"

    print(get_low())
    print("-------------------------------\nThird task:\n")

    @log('log.txt')
    @encrypt(2)
    def get_low():
        return "Get get get low"

    print(get_low())
    print("-------------------------------\nFourth task:\n")

    @performance('log.txt')
    def something_heavy():
        time.sleep(2)
        return "I am done!"

    print(something_heavy())