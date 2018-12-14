# -*- coding: UTF-8 -*-
import requests
import mysql.connector
import json


def fun(index):
    response = requests.get(
        'http://aimai.wgzapp.net/index/index?page=' + str(index) + '&token=4bf602ac7db7d4c3&ajax=cross7ceb971fb8863')
    re_content = response.content
    jo = json.loads(re_content[19:len(re_content) - 2])['result']

    for j in jo:
        # 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
        cnn = mysql.connector.connect(user='root', passwd='root', database='testdb')
        # 使用cursor()方法获取操作游标
        cursor = cnn.cursor()
        cursor.execute(
            'insert  into goods (id,gid,site,cate,title,url,price,prime,ratio,final_sales,thumb,coupon_money,coupon_total,coupon_latest,coupon_url,stoptime,dateline,timeline,choice) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            (
                j['id'], j['gid'], j['site'], j['cate'], j['title'], j['url'], j['price'], j['prime'], j['ratio'],
                j['final_sales'], j['thumb'], j['coupon_money'], j['coupon_total'], j['coupon_latest'], j['coupon_url'],
                j['stoptime'], j['dateline'], j['timeline'], j['choice']))
        cnn.commit()
        cnn.close()
    print(str(index) + '页已保存')
    index2 = index + 1
    response = requests.get(
        'http://aimai.wgzapp.net/index/index?page=' + str(index2) + '&token=4bf602ac7db7d4c3&ajax=cross7ceb971fb8863')
    re_content = response.content
    jo2 = json.loads(re_content[19:len(re_content) - 2])['result']
    if jo2 != '':
        fun(index2)


if __name__ == '__main__':
    fun(1)
