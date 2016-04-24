# -*- coding: utf-8 -*-

"""
无线端报价接口action
"""


import tornado.gen

# MatchNearFlight 算是business, 这一个应该被移出.
from util.nearflight import MatchNearFlight
from util.baseclass import put_post_request_into_ioloop
from util.baseclass import put_get_request_into_ioloop

from util.baseclass import AsyncRequest


from context import config


def is_direct_city(str_from, str_to):
    """
    检查str_from -> str_to 是否为直达城市
    :return:
    True: 是直达城市
    False: 不是直达城市
    """
    return True


def parser_hq_price(context):
    pass



@tornado.gen.coroutine
def fetch_hq_price(context, str_from, str_to, str_date):
    """
    获取hq服务的报价信息
    :return:
    """
    url = "http://%s/fcgi-bin/hqquery_serv?hqfrom=%s&hqto=%s&df=%s&dt=%s&type=text" % (context["options"].hq_server_url, str_from, str_to, str_date, str_date)
    ok, result = yield put_get_request_into_ioloop(context, url)
    if ok:
        for line in result.split("\n"):
            items = line.split("\t")
            if items != [] and items[2] == str_date:
                 tornado.gen.Return((items[0], items[1], items[2], items[3], items[4]))
    else:
        tornado.gen.Return(None)



# def fetch_near_flights(context, funcs, str_from, str_to, str_date, queryid, int_type):
#     """
#     funcs[""]
#     """

@tornado.gen.coroutine
def fetch_near_flights(context, hq_func, str_from, str_to, str_date, queryid, int_type):
    """
    获取临近航班,先使用库存中的城市距离的数据,计算出临近航班的距离
    从行情服务中计算出最低价,拼接生成最后的临近航班的结果数据
    对于这个hq_func,可以在单元测试的时候,方便的替换mock(因为默认的python mock类并不支持yield)
    :return:
    """
    body = {
        "error": 2,
        "errmsg": "NEAR",
        "nearinfo" : {
            "is_match": 0,
            "flightInfo":[]
        }
    }

    mnf = MatchNearFlight()
    body["nearinfo"]["type"] = int_type
    body["nearinfo"]["distance"] = mnf.distances(str_from, str_to)

    if  mnf.is_short_250(str_from, str_to):
        body["nearinfo"]["reason"] = "TOONEAR"
        raise tornado.gen.Return(body)
    else:
        t_near_citys = mnf.find_t_near_city(str_from, str_to)
        for item in t_near_citys:
            result = yield hq_func(context, item["1"][0], str_to, str_date)
            if result != None:
                temp = {
                    "from":item["1"][0],
                    "to": item["1"][1],
                    "date": str_date,
                    "distance": item["1"][2],
                    "dis": result[3],
                    "price": result[4]

                }
                body["nearinfo"]["flightInfo"].append(temp)

        f_near_citys = mnf.find_f_near_city(str_from, str_to)
        for item in f_near_citys:
            result = yield hq_func(context, item["1"][0], str_to, str_date)
            if result != None:
                temp = {
                    "from":item["2"][0],
                    "to": item["2"][1],
                    "date": str_date,
                    "distance": item["2"][2],
                    "dis": result[3],
                    "price": result[4]
                }
                body["nearinfo"]["flightInfo"].append(temp)
                body["nearinfo"]["is_match"] = 1
                raise tornado.gen.Return(body)

        else:
            body["nearinfo"]["reason"] = "NOMATCH"
            raise tornado.gen.Return(body)


@tornado.gen.coroutine
def refresh_sites(context, str_from, str_to, str_date, queryid, sites):
    """
    刷新这些站点的报价
    """

    url = "http://%s/v2.0/services/crawlerworker/fcs/%s%s%s?queryid=%s&action=refresh" % (config.fcs_crawler_address, str_from, str_to, str_date, queryid)
    body = '-'.join(sites)
    yield put_post_request_into_ioloop(context, url, body)



class HqRequest(AsyncRequest):

    def __init__(self, context):
        self.context = context

    def format_request_url(self, params):
        url = "http://%s/fcgi-bin/hqquery_serv?hqfrom=%s&hqto=%s&df=%s&dt=%s&type=text" % (config.hq_server_url, params["str_from"], params["str_to"], params["str_date"], params["str_date"])
        return url

    def parser_response(self, response, str_date):
        for line in response.split("\n"):
            items = line.split("\t")
            if items != [] and items[2] == str_date:
               return (items[0], items[1], items[2], items[3], items[4])
        else:
            return None


    @tornado.gen.coroutine
    def fetch(self, params):
        """
        获取行情数据,如果成功,返回FTD,航线,最低价
        :param params:
        :return:
        """
        url = self.format_request_url(params)
        ok, response = yield put_get_request_into_ioloop(self.context, url)
        if ok:
            self.parser_response(response, params["str_date"])
        else:
            tornado.gen.Return(None)
