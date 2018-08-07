# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql




class ShenpiPipeline(object):

    def process_item(self, item, spider):
        #链接数据库
        DBKWARGS=spider.settings.get('DBKWARGS')
        conn=pymysql.connect(**DBKWARGS)

        #创建游标
        cur=conn.cursor()
        #插入数据
        sql=("INSERT INTO CivilExplosive (compay,carNo,data,state)VALUES(%s,%s,%s,%s)")
        lis=(item['compay'],item['carNo'],item['data'],item['state'])

        #添加判断
        try:
            cur.execute(sql,lis)
        except Exception as e:
            print("insert error",e)
            conn.rollback()     #错误回滚
        else:
            conn.commit()

        cur.close()
        conn.close()

        return item




# class MysqlTwistedPipline(object):
#     def __int__(self,dbpool):
#         self.dbpool=dbpool
#
#     @classmethod
#
#     def from_settings(cls,settings):
#         dbparms=dict(
#             host=settings["MYSQL_HOST"],
#             user=settings["MYSQL_USER"],
#             passwd=settings["MYSQL_PASSWORD"],
#             db=settings["MYSQL_DBNAME"],
#             charset="utf8",
#             cussorclass=pymysql.cursors.DictCursor,
#             use_unicode = True
#         )
#
#         dbpool = pymysql.connect("pymysql", **dbparms)
#         return cls(dbpool)
#
#     def process_item(self,item,spider):
#         # 使用twisted将mysql插入变成异步执行
#         query = self.dbpool.runInteraction(self.do_insert, item)
#         query.addErrback(self.handle_error)  # 处理异常
#
#     def handle_error(self, failure):
#         print(failure)
#
#
#
#
#     def do_insert(self, cursor, item):
#         # 执行具体的插入
#         # 根据不同的item 构建不同的sql语句并插入到mysql中
#         insert_sql, params = item.get_insert_sql()
#         cursor.execute(insert_sql, params)

