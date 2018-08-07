"""
@author:fei
@date:2018-7-5
@brief:链接Redis数据库，获取验证码
"""

import redis


class RedisClient(object):
    """获取验证码"""

    pool = redis.ConnectionPool(host='172.16.33.4', password='REDIS123', port=6379, db=2, decode_responses=True)
    r = redis.Redis(connection_pool=pool)

    def get_code(self, phone):
        code = self.r.get(phone)
        return code


if __name__ == '__main__':
    r = RedisClient()
    b = r.get_code('15822816936')
    print(b)
