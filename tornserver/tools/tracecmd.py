# -*- coding: utf-8 -*-

"""
使用命令行直接调用三方接口,方便及时调试和定位错误
"""

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--from", dest="str_from", help="from")
parser.add_option("-t", "--to", dest="to", help="to")
parser.add_option("-d", "--date", dest="date", help="date like 20160627")
parser.add_option("-s", "--site", dest="site", help="flagship site")
parser.add_option("-e", "--env", dest="env", help="environment", default="test")


if __name__ == "__main__":
    (options, args) = parser.parse_args()