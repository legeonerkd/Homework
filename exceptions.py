# def foo():
#     try:
#         return a / b
#     except ...

def div(a: int, b: int) -> float:
    # return a / b
    try:
        # foo()
        # return a / b
        # raise "Hello"
        raise ZeroDivisionError()
    except ValueError:
        print('value error')
    except TypeError:
        print('type error')
    except IndexError:
        print('index error')
    # except ZeroDivisionError:
    #     print("Could not divide by zero")

try:
    print(div(10, 0))
# except str as s:
#     print(s)
except ZeroDivisionError:
    print("Could not divide by zero")
# except TypeError:
#         print('type error')