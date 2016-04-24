# -*- coding: utf-8 -*-

import pickle

from baseclass import Singleton


class MatchNearFlight(Singleton):
    """
    计算航线相关距离将会用到的函数
    """

    def load(self, file, ft):
        """
        载入城市距离文件
        :param file:
        :param ft: 文件类型
        :return:
        """

        if ft == "json":
            with open(file, 'rb') as f:
                self.db = pickle.load(f)
        elif ft == "txt":
            self.db = {}
            with open(file) as f:
                for line in f:
                    k, p, q = line.strip().split(",")
                    if k not in self.db:
                        self.db[k] = {}
                    self.db[k][p] = int(q)
        else:
            raise Exception("unknow file type")


    def _distances(self, f, t):
        """
        计算f到t的距离,
        :return
        True, 距离
        False, None
        """

        if f in self.db:
            if t in self.db[f]:
                return True, int(self.db[f][t])
        return False, None

    def distances(self, f, t):
        """
        计算f到t的距离,可以直接返回距离
        :param f:
        :param t:
        :return:
        """
        ok, res = self._distances(f, t)
        if ok:
            return res
        return 0

    def is_short_250(self, f, t):
        """
        判断长度是否小于250
        """

        ok, res = self._distances(f,t)
        if not ok:
            return False
        return res <= 250000


    def find_t_near_city(self, f, t):
        """
        筛选出所有f到t的中介城市X, X为t的临近城市，且
        (f-X) + (X-t)  < 2(f-t)
        按照f-X, X-t的距离进行排序
        """

        li = []
        ok, res = self._distances(f, t)
        if not ok:
            return li

        ft_distance = res
        # 找出t的所有临近城市:
        for k, v in self.db[t].iteritems():
            ok, fk = self._distances(f, k)
            if not ok:
                continue

            if fk + v <= ft_distance*2:
                temp = {}
                temp["1"] = [f, k, fk]
                temp["2"] = [k, t, v]
                li.append(temp)

        li.sort(key = lambda x: x["1"][2] + x["2"][2])
        return li


    def find_f_near_city(self, f, t):
        """
        筛选出所有f到t的中介城市X, X为f的临近城市,且
        (f-X) + (X-t) < 2(f-t)
        按照f-X, X-t的距离进行排序
        """

        li = []
        ok, res = self._distances(f, t)
        if not ok:
            return li

        ft_distance = res
        # 找出f的所有临近城市:
        for k, v in self.db[f].iteritems():
            ok, kt = self._distances(k, t)
            if not ok:
                continue

            if v + kt <= ft_distance*2:
                temp = {}
                temp["1"] = [f, k, v]
                temp["2"] = [k, t, kt]
                li.append(temp)

        li.sort(key = lambda x: x["1"][2] + x["2"][2])
        return li