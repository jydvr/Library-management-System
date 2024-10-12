from flask import Flask, request
import time
from filehandler import BookHandler

class LibraryApp:
    def __init__(self):
        try:
            self.app = Flask(__name__)
            self.book_handler = BookHandler()
            self.calling()
        except Exception as e:
            print(e)
            
    def calling(self):
        @self.app.route('/', methods=['GET'])
        def get_books():
            try:
                print("get_books() started")
                st_time = time.time()
                result = self.book_handler.display()
                fi_time = time.time()
                self.calcprint(st_time, fi_time)
                print("get_books() completed")
                return result
            except Exception as e:
                print(e)

        @self.app.route('/add', methods=['POST'])
        def add_book():
            try:
                print("add_book() started")
                st_time = time.time()
                data = request.get_json()
                result = self.book_handler.add(data)
                fi_time = time.time()
                self.calcprint(st_time, fi_time)
                return result
            except Exception as e:
                print(e)

        @self.app.route('/borrow', methods=['POST'])
        def borrow_book():
            try:
                print("borrow_book() started")
                st_time = time.time()
                data = request.get_json()
                result = self.book_handler.borrow(data)
                fi_time = time.time()
                self.calcprint(st_time, fi_time)
                return result
            except Exception as e:
                print(e)

        @self.app.route('/delete', methods=['POST'])
        def delete_book():
            try:
                print("delete_book() started")
                st_time = time.time()
                data = request.get_json()
                result = self.book_handler.delete(data)
                fi_time = time.time()
                self.calcprint(st_time, fi_time)
                print("delete_book() completed")
                return result
            except Exception as e:
                print(e)
                
        @self.app.route('/returns', methods=['POST'])
        def return_book():
            try:
                print("return_book() started")
                st_time = time.time()
                data = request.get_json()
                result = self.book_handler.returns(data)
                fi_time = time.time()
                self.calcprint(st_time, fi_time)
                print("return_book() completed")
                return result
            except Exception as e:
                print(e)
    def calcprint(self, st_time, fi_time):
        try:
            ex_time = (fi_time - st_time) * 1000  
            self.book_handler.metlog.info(f"Get connection to the SQL server | Start Time: {st_time:.4f} | End Time: {fi_time:.4f} | Execution Time: {ex_time:.4f} ms")
            self.book_handler.logger.info(f"Connected to the MySQL server")
        except Exception as e:
            print(e)

    def run(self):
        try:
            self.app.run(debug=True)
        except Exception as e:
            print(e)
if __name__ == "__main__":
    try:
        app = LibraryApp()
        app.run()
    except Exception as e:
        print(e)