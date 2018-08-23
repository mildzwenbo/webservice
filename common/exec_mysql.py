import pymysql
from common.log import logger
import threading
import configparser
from common.get_path import GetPath
each = GetPath()
mysql_conf_path = each.get_conf_path('mysql.ini')
mutex=threading.Lock()
mutex.acquire() # 上锁，防止多线程下出问题
conf = configparser.ConfigParser()
conf.read(mysql_conf_path, encoding='utf-8')
# if conf.get('select', 'select') == '1':
#     host = conf.get('testmysql', 'host')
#     port = int(conf.get('testmysql', 'port'))
#     user = conf.get('testmysql', 'user')
#     passwd = conf.get('testmysql', 'passwd')
#     db = conf.get('testmysql', 'db')
# else:
#     host = conf.get('mysql', 'host')
#     port = int(conf.get('mysql', 'port'))
#     user = conf.get('mysql', 'user')
#     passwd = conf.get('mysql', 'passwd')
#     db = conf.get('mysql', 'db')
host = conf.get('mysql', 'host')
port = int(conf.get('mysql', 'port'))
user = conf.get('mysql', 'user')
passwd = conf.get('mysql', 'passwd')
db = conf.get('mysql', 'db')
mutex.release()


class ExecMysql():
    log = logger

    def select_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            row = cursor.fetchall()
            return row
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def insert_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def delete_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()

    def update_mysql(self, sql):
        try:
            connect = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=passwd,
                db=db,
            )
            cursor = connect.cursor()
            cursor.execute(sql)
            connect.commit()
        except Exception as msg:
            self.log.info(str(msg))
        finally:
            cursor.close()
            connect.close()


def fun_select():
    a = ExecMysql()
    sql = "SELECT * FROM run_status;"
    b = a.select_mysql(sql)
    for i in b:
        print(i)


if __name__ == '__main__':
    mysql = ExecMysql()
    # 查询
    select_sql = "SELECT status FROM run_status WHERE name='test_g_release_product_clcik';"
    result = mysql.select_mysql(select_sql)[0][0] #得到的为元组
    print(result)
    # for i in result:
    #     print(i[1])
    # print('-' * 100)
    # 插入数据
    # insert_sql = "INSERT INTO run_status(name, status) VALUE ('status1', '1234');"
    # mysql.insert_mysql(insert_sql)
    # fun_select()
    # print('-'*100)
    # # 更新数据
    # update_sql = "UPDATE trade SET user='fei' WHERE id=32;"
    # mysql.update_mysql(update_sql)
    # fun_select()
    # print('-' * 100)
    # #删除数据
    # delete_sql = "DELETE FROM trade WHERE id=32;"
    # mysql.delete_mysql(delete_sql)
    # fun_select()

    # mysql.update_mysql("UPDATE run_status SET status='0' WHERE name='test_g_release_product_clcik';")

#
