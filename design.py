# -*- coding: utf-8 -*-


"""
python代码写多了，你会看到各种各样的单例模式。
实际上，我们去思考一下单列模式本身的作用，在整个程序中，只有一份实例。首先这个一份实例，是指进程级别的，也就是说，你的各个逻辑级别的代码，需要引用同一个对象。
所以这种引用的级别，实际上是动态的，而那种基于包的导入机制,引用函数才算是静态的。
"""

"""
在公司中有使用如下代码，完成单例模式,如果想引用对象，那么只需要:

在定义一个类的时候，使用此装饰器进行装饰。
之后在引用的时候，直接这样就可以了。
Cxxc().getInstance()
但是，问题是什么，你发现了么？问题这个类已经不是一个类了，变成了一个函数，虽然说在python中函数也是对象，但是你不能继承关系全部都乱套了，包括什么调用父类构造函数之类的。

@singleton
class availsiteTimer(BaseTimer):
    def __init__(self):

所以说上面这段代码，你的__init__中，想要调用他的super函数，就会报错，并告诉你函数不能这么玩。


关于多线程锁，实际上，在tornado中，使用这些单例模式，根本不许需要考虑锁的问题。因为它是单线程运行的。
"""
def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton



def main():
    pass

if __name__ == "__main__":
    main()
