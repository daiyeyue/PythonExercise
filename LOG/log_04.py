'''
使用logging的四大组件来实现日志的功能
--打印函数执行的时间、错误的等级和错误的消息
--使用装饰器
--不同的日志，要记录不同等级的日志消息
'''

import logging

logger_daiye = logging.getLogger("mylogger")

logger_daiye.setLevel(logging.DEBUG)

#handler
#TimeRotationHandler、FileHandler
debug_handler = logging.FileHandler("1024_debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handler = logging.FileHandler("1024_error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger_daiye.addHandler(debug_handler)
logger_daiye.addHandler(error_handler)

def log(func):
    def wrapper(*args, **kwargs):
        logger_daiye.debug("this is a debug info")
        logger_daiye.error("this is a error info")
        return func(*args, **kwargs)
    return wrapper

def loghigher(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger_daiye.debug(text)
            logger_daiye.error(text)
            return func(*args, **kwargs)
        return wrapper
    return decorator

#按照函数不同，在日志中打印不同的东西
@log
def abc():
    print("abc done")

@loghigher("this is main done")
def main():
    print("main done")

abc()
main()

###一般实际工作中，把logging封装成一个装饰器