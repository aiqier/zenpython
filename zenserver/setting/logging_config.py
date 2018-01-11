#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
import datetime

from tornado import ioloop

from util.simtools import get_diff_time


REFRESH_LOG_TIME = "00:00:00"

def init_logger_file_handler(log_path, logger_name):
    """
    写入文件的logger
    :param logger:
    :return:
    """
    logger = logging.getLogger(logger_name)
    log_formatter = logging.Formatter("%(asctime)s %(levelname).1s [%(process)d] %(filename)s:%(lineno)d - %(message)s")
    log_filename = "%s/%s.log.%s" % (log_path, logger_name, datetime.datetime.now().strftime("%Y-%m-%d"))
    handler = logging.FileHandler(log_filename)
    handler.setLevel(logging.INFO)
    handler.setFormatter(log_formatter)

    for _handler in logger.handlers:
        logger.removeHandler(_handler)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def init_logger_console_handler(logger_name):
    """
    写入到屏幕的log
    :param logger:
    :return:
    """
    logger = logging.getLogger(logger_name)
    log_formatter = logging.Formatter("%(asctime)s %(filename)s:%(lineno)d - %(message)s")

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)

def init_product_logger(log_path):
    """
    初始化生产环境的log配置
    :return:
    """
    init_logger_file_handler(log_path, "business")

def init_test_logger(log_path):
    """
    初始化集成测试环境下的log配置
    :return:
    """
    pass


def init_debug_logger(log_path):
    """
    初始化debug环境的log配置
    :return:
    """
    init_logger_console_handler("business")

def period_init_log_task(task):
    global REFRESH_LOG_TIME
    init_product_logger()
    task.stop()
    refresh_task = ioloop.PeriodicCallback(lambda: period_init_log_task(refresh_task), get_diff_time(REFRESH_LOG_TIME))
    refresh_task.start()

def init_log_task():
    global REFRESH_LOG_TIME
    init_product_logger()
    init_task = ioloop.PeriodicCallback(lambda: period_init_log_task(init_task), get_diff_time(REFRESH_LOG_TIME))
    init_task.start()

