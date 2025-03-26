def vilidate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args,*kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be  int or float")
        result = fn(*args, **kwargs)
        return result

    return wrapper
@vilidate_args
def sum_nums(a, b):
    return a + b
try:
    print(sum_nums(7, 2))
    print(sum_nums(10.5, 2.3))
    print(sum_nums(a=1.5, b="2.3"))
except ValueError as e:
    print(e)
