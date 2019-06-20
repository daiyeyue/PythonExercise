'''
装饰器
- 使用装饰器，打印函数执行的时间

'''

import logging

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format)
def log(func):
    def wrapper(*arg, **kwargs):
        logging.error("this is error message")
        return func(*arg, **kwargs)
    return wrapper

@log
def abc():
    print("test done")

abc()
