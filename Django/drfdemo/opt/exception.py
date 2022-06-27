from rest_framework.views import exception_handler
from rest_framework.response import Response

def exception_handlerss(exc, context):
    """
    自定义异常函数
    :param exc：本次发生异常对象，对象
    :param context：本次发生异常上下文信息，字典
    所谓执行上下文就是python 解释器在执行代码保存内存变量，函数，类，对象，变量，等一系列信息
    :return:
    """
    # 让 drf 能把处理都处理了，假如处理不了返回None
    resp = exception_handler(exc, context)

    if resp == None:
        """
        当前异常drf 没有处理
        """
        if isinstance(exc, ZeroDivisionError):
            resp = Response({"detial":'0不能作为除数'})

    return resp
