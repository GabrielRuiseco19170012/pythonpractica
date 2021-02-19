import pymysql


class DatabaseMySql:

    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='pymysql'
        )
        self.cursor = self.connection.cursor()
        print("Established Connection with MySql")

    def sendData(self, data, table):
        sqlUsr = "INSERT INTO `%s`" % table + "(Name,LastName,Age) VALUES (%s,%s,%s)"
        sqlMat = "INSERT INTO `%s`" % table + "(Name,Quantity,Date_Out,Date_in) VALUES (%s,%s,%s,%s)"
        sqlList = "INSERT INTO UserMaterials(MaterialID,UserID,Quantity) VALUES (%s,%s,%s)"
        try:
            if table == "Users":
                self.cursor.execute(sqlUsr, (data.name, data.lastName, int(data.age)))
                self.connection.commit()
            elif table == "Materials":
                self.cursor.execute(sqlMat, (data.name, int(data.quantity), data.date_out, data.date_in))
                self.connection.commit()
            else:
                self.cursor.execute(sqlList, (data["mid"], data["uid"], data["quantity"]))
                self.connection.commit()
        except Exception as e:
            raise

    def getAllData(self, table):
        sql = 'SELECT * FROM `%s`' % table
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            raise

    def getOneData(self, column, table, value):
        sql = 'SELECT * FROM `%s`' % table + ' WHERE `%s`' % column + ' = %s'
        try:
            self.cursor.execute(sql, value)
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            raise

    def getManyData(self, column, table, value):
        sql = 'SELECT * FROM `%s`' % table + ' WHERE `%s`' % column + ' = %s'
        try:
            self.cursor.execute(sql, value)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            raise

    def getUMList(self, mid, uid):
        sql = 'SELECT * FROM UserMaterials WHERE MaterialID = %s AND UserID = %s'
        try:
            self.cursor.execute(sql, (mid, uid))
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            raise

    def updateData(self, table, column, updCol, newVal, idVal):
        sql = ""
        if table == "Users":
            sql = 'UPDATE Users SET `%s`' % updCol + ' = %s' + ' WHERE `%s`' % column + ' = %s'
        elif table == "UserMaterials":
            sql = 'UPDATE UserMaterials SET `%s`' % updCol + ' = %s' + ' WHERE `%s`' % column + ' = %s'
        elif table == "Materials":
            sql = 'UPDATE Materials SET `%s`' % updCol + ' = %s' + ' WHERE `%s`' % column + ' = %s'
        else:
            print("tabla no encontrada")
        try:
            self.cursor.execute(sql, (newVal, idVal))
            self.connection.commit()
        except Exception as e:
            raise

    def deleteData(self, table, column, idval):
        sql = 'DELETE FROM `%s`' % table + 'WHERE `%s`' % column + ' = %s'
        try:
            self.cursor.execute(sql, idval)
            self.connection.commit()
        except Exception as e:
            raise
