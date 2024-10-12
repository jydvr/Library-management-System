import mysql.connector as myConn
import json
from collections import OrderedDict
import meteringlog, customlogger
import pandas as pd
import queries

class BookHandler:
    def __init__(self):
        try:
            self.met = meteringlog.Metering()
            self.metlog = self.met.get_log()
            self.custom_logger = customlogger.CustomLogger()
            self.logger = self.custom_logger.get_logger()
        except Exception as e:
            print(e)
    def connect(self):
        try:
            mydb = myConn.connect(
                host="localhost",
                user="root",
                password="123123",
                database="pay"
            )
            return mydb
        except Exception as e:
            self.logger.error(f"Error accessing database credentials: {str(e)}")
            raise

    def calcprint(self, st_time, fi_time):
        try:
            ex_time = (fi_time - st_time) * 1000  
            self.metlog.info(f"Execution Time: {ex_time:.4f} ms")
            self.logger.info(f"Operation completed")
        except Exception as e:
            print(e)

    def add(self, data):
        try:
            title = data["title"]
            if not title:
                return {"message":"Give correct book name"}
            mydb = self.connect()
            cursor = mydb.cursor(dictionary=True)
            dicts = self.display()
            for item in json.loads(dicts)['data']:
                if item['title'] == title:
                    return {"message": "Cannot add same book"}
            query = queries.add
            cursor.execute(query, (title, True, "Null"))
            mydb.commit()
            cursor.close()
            return {"message": "Added a new book"}
        except Exception as e:
            self.logger.error(f"Error adding book: {str(e)}")
            return {"message": "Unsuccessful"}

    def display(self):
        try:
            print("display() started")
            mydb = self.connect()
            cursor = mydb.cursor(dictionary=True)
            cursor.execute(queries.prints)
            books = cursor.fetchall()
            cursor.close()
            df = pd.DataFrame(books, columns=["id", "title", "available", "user"])
            print(df)
            result = df.to_dict(orient="records")
            print("display() completed")
            return json.dumps({"data": result})
           
        except Exception as e:
            self.logger.error(f"Error displaying books: {str(e)}")
            return {"message": "Unsuccessful"}

    def borrow(self, data):
        try:
            print("borrow() started")
            title = data["title"]
            user = data["user"]
            mydb = self.connect()
            cursor = mydb.cursor(dictionary=True)
            dicts = self.display()
            for item in json.loads(dicts)['data']:
                if item['title'] == title and item['available'] == 1:
                    query = queries.borrow
                    cursor.execute(query, (False, user, title, True))
                    mydb.commit()
                    cursor.close()
                    print("borrow() completed")
                    return {"message": "Borrowed a book"}
            print("borrow() completed")
            return {"message": "Book is not available"}
        except Exception as e:
            self.logger.error(f"Error borrowing book: {str(e)}")
            return {"message": "Unsuccessful "}

    def returns(self, data):
        try:
            print("returns() started")
            title = data["title"]
            mydb = self.connect()
            cursor = mydb.cursor(dictionary=True)
            
            dicts = self.display()
            for item in json.loads(dicts)['data']:
                if title in item["title"] and item['available'] == 0:
                    query = queries.returns
                    cursor.execute(query, (True, "Null", title))
                    mydb.commit()
                    cursor.close()
                    print("returns() completed")
                    return {"message": "Returned the book"}
            for item in json.loads(dicts)['data']:
                if title in item["title"] and item["available"]==1:
                    print("returns() completed")
                    return {"message": "Book is already available"}
            for item in json.loads(dicts)['data']:   
                if title not in item["title"]:
                    print("returns() completed")
                    return {"message":"Book is not present"}
        except Exception as e:
            self.logger.error(f"Error returning book: {str(e)}")
            return {"message": "Unsuccessful"}

    def delete(self, data):
        try:
            print("delete() started")
            title = data["title"]
            mydb = self.connect()
            cursor = mydb.cursor(dictionary=True)

            dicts = self.display()
            for item in json.loads(dicts)['data']:
                if title in item['title'] and item['available']==1:
                    query = queries.delete
                    cursor.execute(query, (title,))
                    mydb.commit()
                    cursor.close()
                    print("delete() completed")
                    return {"message": "Deleted a book"}
            for item in json.loads(dicts)['data']:
                if title in item['title'] and item['available']==0:
                    print("delete() completed")
                    return{"message":"Cannot delete a book that is borrowed"}
            for item in json.loads(dicts)['data']:
                if title not in item['title']:
                    print("delete() completed")
                    return {"message": "Cannot delete a book that doesn't exist"}
        except Exception as e:
            self.logger.error(f"Error deleting book: {str(e)}")
            return {"status": False, "message": "Unsuccessful", "data": str(e)}
