#this module is used for database connection and querying

import psycopg2
import time
import random
import string
# from . import configurations as conf

# def randomString(stringLength=10):
#     """Generate a random string of fixed length """
#     random.seed(time.time())
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(stringLength))

class DbConfig:
    def __init__(self, db_ip, db_name, db_port, db_username, db_password):
        self.db_ip = db_ip
        self.db_name = db_name
        self.db_port = db_port
        self.db_username = db_username
        self.db_password = db_password
        self.comboUsed = []


    def ConnectDb(self):  # self,db_ip,db_name, db_port, db_username, db_password):
        try:
            self.conn = psycopg2.connect(
                "dbname='" + self.db_name + "' user='" + self.db_username + "' host='" + self.db_ip + "' password='" + self.db_password + "' port=" + str(
                    self.db_port) + "")
            return True
        except Exception as e:
            print(e)
            return False

    # def returnedFormattedQuery(self, query, vare = None):
    #     cursor = self.conn.cursor()
    #     result = cursor.mogrify(query, vare)
    #     cursor.close()
    #     return result
    def DbResultsQuery(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            cursor.close()
            # self.conn.commit()
            return res
        except Exception as e:
            self.refreshDbConenction()
            raise e

    def DbResultsQuery(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            cursor.close()
            # self.conn.commit()
            return res
        except Exception as e:
            self.refreshDbConenction()
            raise e
    # def returnCursorQuery(self, query):
    #     while True:
    #         cur_name = str(random.randint(1,100)) + str(random.randint(1,100)) + str(random.randint(1,100))
    #         if cur_name not in self.comboUsed:
    #             self.comboUsed.append(cur_name)
    #             break
    #     cursor = self.conn.cursor(cur_name)
    #     cursor.execute(query)
    #     return cursor

    # def handleNewPoiInsertionWithImage(self, values):
    #     try:
    #         cursor = self.conn.cursor()
    #         # Getting value for the new poi id
    #         cursor.execute("""SELECT column_default from information_schema.columns
    #         where table_name='pois_v6' and table_schema='public' and column_default is not null and column_name='id'""")
    #         sequence= cursor.fetchall()[0][0]
    #         cursor.execute("select {0};".format(sequence))
    #         poi_id = cursor.fetchall()[0][0]
    #         # Inserting new point into pois v6
    #         insert_query = "INSERT INTO {0} (id, name,name_displ,tpl_subcat,priority,email,telephone,url,fax,geom,primary_source,secondary_source,data_status,source_id,tags,descriptio) values ({1}, %s,%s,%s,%s,%s,%s,%s,%s,ST_GeomFromText(%s,3857),%s,%s,%s,%s,%s,%s)".format(conf.data_table, poi_id)
    #         cursor.execute(insert_query, values)
    #         self.conn.commit()
    #         return poi_id
    #     except Exception as e:
    #         self.refreshDbConenction()
    #         raise e

    def DbModifyQuery(self,query, vare=None):
        # print(query)
        # return
        try:
            cursor = self.conn.cursor()
            print(cursor.mogrify(query, vare))
            cursor.execute(query, vare)
            cursor.close()
            self.conn.commit()
        except Exception as e:
            self.refreshDbConenction()
            raise e

    def commitConnection(self):
        self.conn.commit()

    def releaseDbConnection(self):
        self.conn.close()

    def DbResultsQueryForFunction(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.close()
        self.conn.commit()


    def refreshDbConenction(self):
        try:
            self.releaseDbConnection()
        except:
            pass
        self.ConnectDb()
