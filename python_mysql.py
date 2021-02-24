import pymysql
class python_mysql:
    def __init__(self):
        #数据库连接
        self.database = pymysql.connect(host="localhost", user="root", database="testing1")
        self.cursor = self.database.cursor()

    def insert(self):
        #插入数据
        sql = 'insert into my_first_mysql_table values ("cpy2", "18575718283")'
        self.cursor.execute(sql)
        self.database.commit()
        self.database.close()

    def change(self):
        #更改数据
        sql = "update my_first_mysql_table set phone='15623228987' where company='cpy1'"
        self.cursor.execute(sql)
        self.database.commit()
        # print(self.cursor.fetchall())
        self.database.close()

    def lookupvalue(self):
        #查找数据
        sql = "select * from my_first_mysql_table"
        self.cursor.execute(sql)
        # self.database.commit()
        print(self.cursor.fetchall())
        self.database.close()

    def delete(self):
        sql = "delete from my_first_mysql_table where phone = '18575718283'"
        self.cursor.execute(sql)
        self.database.commit()
        self.database.close()

if __name__ == '__main__':
    solution = python_mysql()
    solution.insert()
    solution.change()
    solution.lookupvalue()
    solution.delete()