#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging

from util.baseclass import BaseHandler

from hello_action import add

logger = logging.getLogger(__name__)

class HelloWorld(BaseHandler):
    def get(self):
        logger.info("TEST")
        result = add(3, 4)
        self.write("OK: %s" % result)