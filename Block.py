# -*- coding: UTF-8 -*-
'''
@Author ：wangjie
@Date   ：2020/1/5 19:36
@Desc   ：
'''
import hashlib
import json


class Block:
    def __init__(self, timestep, data, previous_hash=''):
        '''
        区块链初始化
        :param timestep: 创建时间
        :param data:  区块数据
        :param previous_hash: 上一个区块的哈希值
        '''
        self.previous_hash = previous_hash
        self.timestep = timestep
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        '''
        计算区块的hash值
        :return:
        '''
        # 将区块信息拼接后生成sha256的hash值
        raw_str = str(self.previous_hash) + str(self.timestep) + str(json.dumps(self.data, ensure_ascii=False))   #第二个参数指定可以输出中文
        sha256 = hashlib.sha256()
        sha256.update(raw_str.encode('utf-8'))
        hash = sha256.hexdigest()   #返回16进制
        return hash