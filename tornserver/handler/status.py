# -*- coding: utf-8 -*-

"""
服务器状态
"""

import tornado.web


class StatusHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Status Ok")