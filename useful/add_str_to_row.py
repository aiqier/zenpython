# -*- coding: utf-8 -*-

"""
为文本行的收尾添加字符串
"""


def add_head(s, line):
    return s + line

def add_tail(s, line):
    return line + s

def iter_file(rfilename, wfilename, begin=1, end=-1, funcs=None):
    with open(rfilename, "r") as rf:
        with open(wfilename, "w") as wf:
            for line in rf:
                if begin == end:
                    break
                begin +=1
                for func in funcs:
                    line = func(line)
                wf.write(line)


def addn():
    i = 0
    def func():
        p = i
        i += 1
        return p
    return func

def main(rfilename, wfilename, begin=1, end=-1):
    func1 =