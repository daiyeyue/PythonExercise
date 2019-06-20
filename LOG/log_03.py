'''
使用装饰器，根据不同的函数，传入的日志不同
'''
import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format)
# def log(func):
#     def wrapper(*arg, **kwargs):
#         logging.error("this is error message")
#         return func(*arg, **kwargs)
#     return wrapper

def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.error(text)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log("abc")
def abc():
    print("test done")

@log("main")
def main():
    print("main done")

abc()
main()