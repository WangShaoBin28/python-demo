# -*- coding: UTF-8 -*-
import mysql.connector
import demo1

# 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
cnn = mysql.connector.connect(user='root', passwd='root', database='testdb')
# 使用cursor()方法获取操作游标
cursor = cnn.cursor()
# 使用execute方法执行SQL语句
# cursor.execute('insert into user (id, name) values (%s, %s)', (None, 'Michae2'))
# cnn.commit()
cursor.execute("SELECT * from user")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchall()
print("Database version : %s " % str(data))
# 执行sql语句
cnn.close()

