# -*- coding: UTF-8 -*-
'''
@Author ：wangjie
@Date   ：2020/1/5 19:48
@Desc   ：
'''

from 区块链.Block import Block
import time

class BlockChain:
    def __init__(self):
        #初始化区块链
        self.chain = [self._creat_genesis_block()]

    @staticmethod
    def _creat_genesis_block():
        '''
        生成创世区块
        :return: 创世区块
        '''
        timestep = time.mktime(time.strptime('2020-01-05 00:00:00', '%Y-%m-%d %H:%M:%S'))
        block = Block(timestep, [], '')
        return block

    def get_lastest_block(self):
        '''
        获取最后一个也就是最新的区块
        :return:
        '''
        return self.chain[-1]

    def add_block(self, block):
        '''
        添加区块
        :param block: 要添加的区块
        :return:
        '''
        block.previous_hash = self.get_lastest_block().hash
        block.hash = block.calculate_hash()
        self.chain.append(block)

    def verify_blockchain(self):
        '''
        校验区块是否完整，是否被篡改过
        :return:
        '''
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                # 当前区块哈希值不等于计算出来的hash
                return False
            if current_block.previous_hash != previous_block.calculate_hash():
                # 当前区块记录的上个区块的hash不等于上个区块计算出来的hash，上个区块有问题
                return False
        return True

if __name__ == '__main__':
    # 测试
    blockChain = BlockChain()
    #添加区块
    blockChain.add_block(Block(time.time(), {'amount': 100}))
    blockChain.add_block(Block(time.time(), {'amount': 200}))
    # 校验区块链
    print('有效！' if blockChain.verify_blockchain() else "无效！")
    # 尝试修改区块链
    blockChain.chain[1].data = {'amount': 50}
    # 再次检验
    print('有效！' if blockChain.verify_blockchain() else "无效！")
