# -*- coding: utf-8 -*-

"""
和ioloop有关的工具
"""

import tornado.web
import tornado.gen
import tornado.httpclient

from tornado import ioloop

import logging

logger = logging.getLogger(__name__)

# 这两个方法与其写成函数,不如做成一个对象,提供get和post方法.

@tornado.gen.coroutine
def put_get_request_into_ioloop(context, url, origin=False):
    """
    把一个异步get请求扔到tornado ioloop中
    :param url: 请求url
    :param handler_id: 处理id
    :param origin: 是否日志请求和响应原串
    :return:
    True, 返回结果
    False, None
    """
    if origin:
        logger.info("Request:%s\t%s" % (context["handler_id"], url))
    try:
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch(url)
        if origin:
            logger.info("Response:%s\t%s" % (context["handler_id"], response.body))
    except:
        logger.error("ErrorRequest:%s\t%s" % (context["handler_id"], url), exc_info=True)
        raise tornado.gen.Return((False, None))
    else:
        raise tornado.gen.Return((True, response.body))


@tornado.gen.coroutine
def put_post_request_into_ioloop(context, url, body, origin=False):
    """
    把一个异步post请求扔到tornado ioloop中
    :param url: 请求url
    :param body: 请求体
    :param handler_id: 处理id
    :param origin: 是否日志请求和响应原串
    :return:
    True, 返回结果
    False, None
    """
    if origin:
        logger.info("Request:%s\t%s\t%s" % (context["handler_id"], url, body))
    try:
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield client.fetch(url, method="POST", body=body)
        if origin:
            logger.info("Response:%s\t%s" % (context["handler_id"], response.body))
    except:
        logger.error("ErrorRequest:%s\t%s\t%s" % (context["handler_id"], url, body), exc_info=True)
        raise tornado.gen.Return((False, None))
    else:
        raise tornado.gen.Return((True, response.body))