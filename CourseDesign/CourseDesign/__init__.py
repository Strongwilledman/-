import pymysql

pymysql.install_as_MySQLdb()
# #打开数据库连接
# db = pymysql.connect("localhost","root","root","orm")
# #获取操作游标
# cursor = db.cursor()
#
# result = cursor.execute("show database")
#
# print(result)
#
# db.close()