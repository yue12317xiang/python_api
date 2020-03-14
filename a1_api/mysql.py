import pymysql
from read_config import Read_Config
class Do_mysql:
        def domysql(self,state='all'):
                do_mysql = {'host':'localhost',
                        'user':'root',
                        'password':'1234',
                        'port':3306,
                        'database':'xbc'
                        }
                # do_mysql = Read_Config().read_config('ceae.config','DB','do_mysql')
                #创建数据库连接
                cnn = pymysql.connect(**do_mysql)
                #创建游标
                cus = cnn.cursor()
                #写sql语句
                
                #执行sql语句
                cus.execute(sql)
                #获取结果
                if state == 1:
                        res = cus.fetchone() #只查询一条语句时用fetchone,数据类型是元组数据类型，查询多条时使用fetchall,数据类型是列表，是以列表嵌套元组的形式展示数据
                else:
                        res = cus.fetchall()
                #关闭游标
                cus.close()
                #关闭连接
                cnn.close()
                return res

if __name__ == '__main__':
        sql = 'select max(id) from goods where id'
        res = Do_mysql().domysql(sql)
        print(res[0])
    
