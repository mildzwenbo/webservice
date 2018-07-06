#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
__author__='hzh'
__time__=2018 / 06 / 27

"""
import pymysql
import time
import os
import paramiko
import platform
import configparser
import threading

from common.get_path import GetPath


# dbUser='root'
# dbPasswd='Cisco123,'
# dbHost='172.16.33.4'
# dbCharset = 'utf8'
# backupDir = '/home/mysql/db_bak'
# dbList = ['boss', 'ruixin']
# sysUser = 'wangyunfei'
# sysPwd = 'Wyf123456'


class MysqlUtil(object):
    mutex = threading.Lock()
    mutex.acquire()
    conf = configparser.ConfigParser()
    conf_ptah = GetPath().get_conf_path('mysql.ini')
    conf.read(conf_ptah, encoding='utf-8')
    if conf.get('select', 'select') == '1':
        db_user = conf.get('test_mysql', 'db_user')
        db_pwd = conf.get('test_mysql', 'db_pwd')
        db_host = conf.get('test_mysql', 'db_host')
        db_charset = conf.get('test_mysql', 'db_charset')
        backup_dir = conf.get('test_mysql', 'backup_dir')
        db_list = conf.get('test_mysql', 'db_list').split(',')
        sys_user = conf.get('test_mysql', 'sys_user')
        sys_pwd = conf.get('test_mysql', 'sys_pwd')
    else:
        db_user = conf.get('test_mysql', 'db_user')
        db_pwd = conf.get('test_mysql', 'db_pwd')
        db_host = conf.get('test_mysql', 'db_host')
        db_charset = conf.get('test_mysql', 'db_charset')
        backup_dir = conf.get('test_mysql', 'backup_dir')
        db_list = conf.get('test_mysql', 'db_list').split(',')
        sys_user = conf.get('test_mysql', 'sys_user')
        sys_pwd = conf.get('test_mysql', 'sys_pwd')
    mutex.release()

    # Mysql连接
    conn = pymysql.connect(db_host, db_user, db_pwd, charset='utf8')
    curs = conn.cursor()

    backup_date = time.strftime("%Y%m%d-%H%M%S")
    # db_list = ['boss', 'ruixin']

    def ssh_linux(self, cmds):
        """
            联机Linux
        """
        try:
            # 创建ssh客户端
            client = paramiko.SSHClient()
            # 第一次ssh远程时会提示输入yes或者no
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(self.db_host, 22, self.sys_user, self.sys_pwd, timeout=20)
            stdin, stdout, stderr = client.exec_command(cmds)
            # 获取命令执行结果,返回的数据是一个list
            result = stdout.readlines()
            return result

        except Exception as e:
            print('Exception', e)
        finally:
            client.close()

    def system_type(self):
        """
        判断系统
        :return:
        """
        systype = platform.system()
        return systype

    def mysql_bck(self):
        """
        备份
        :return:
        """
        curs = MysqlUtil().curs
        conn = MysqlUtil().conn
        localsystye = MysqlUtil().system_type()
        if localsystye == 'Windows':
            for a in self.db_list:
                dbBakSql='mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s/%s/%s_%s.sql' % \
                         (self.db_host, self.db_user, self.db_pwd, a, self.db_charset, self.backup_dir, a, a,
                          self.backup_date)
                bakres = MysqlUtil().ssh_linux(dbBakSql)
                if bakres == []:
                    print(a, 'bak succ!')
                else:
                    print(a, 'bak failed!')
        else:
            for b in self.db_list:
                dbbakSql = 'mysqldump -h%s -u%s -p%s %s --default_character-set=%s > %s/%s/%s_%s.sql' % \
                           (self.db_host, self.db_user, self.db_pwd, b, self.db_charset, self.backup_dir, b, b,
                            self.backup_date)
                res = os.system(dbbakSql)
                if res == 0:
                    print(b, 'bak succ!')
                else:
                    print(b, 'bak failed!')

        curs.close()
        conn.close()

    def mysql_recover(self):
        """
        恢复
        :return:恢复
        """
        curs = self.curs
        conn = self.conn
        localsystye = MysqlUtil().system_type()

        if localsystye == 'Windows' or localsystye == 'Darwin':
            for i in self.db_list:
                cmds = 'ls -rt %s/%s' % (self.backup_dir, i) + '| tail -n 1'
                lastBakfile =self.backup_dir + '/' + i + '/' + "".join(self.ssh_linux(cmds))
                DBrecover='mysql -h%s -u%s -p%s %s < %s' %\
                          (self.db_host, self.db_user, self.db_pwd, i, lastBakfile)
                bakresd = MysqlUtil().ssh_linux(DBrecover)
                if bakresd == []:
                    print(i,'revover succ!')
                else:
                    print(i,'recover failed!')
        else:
            for j in self.db_list:
                cmds = 'ls -rt %s/%s'%(self.backup_dir, j) + '| tail -n 1'
                lastbakfile = self.backup_dir + '/' + j + '/' + os.popen(cmds).readline()
                dbrecover='mysql -h%s -u%s -p%s %s < %s' % (self.db_host, self.db_user,self.db_pwd, j, lastbakfile)
                resource = os.system(dbrecover)
                if resource == 0:
                    print(j, 'resource ok')
                else:
                    print(j, 'resource error!')

        curs.close()
        conn.close()


if __name__ == '__main__':
    m = MysqlUtil()
    m.mysql_recover()

