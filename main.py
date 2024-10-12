import pandas as pd
import requests

class LibraryCLI:
    def __init__(self):
        try:
            self.flag = True
        except Exception as e:
            print(e)

    def run(self):
        try:
            while self.flag:
                self.menu()
        except Exception as e:
            print(e)

    def menu(self):
        try:
            choice = input("Enter\n1: Add book\n2: Borrow book\n3: Return book\n4: Delete book\n5: Display library\n6: Exit\n")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.delete_book()
            elif choice == '5':
                self.display_books()
            elif choice == '6':
                self.flag = False
            else:
                print("Choose from 1-6\n")
        except Exception as e:
            print(e)

    def add_book(self):
        try:
            title = input("Enter book title\n").lower().strip()
            response = requests.post('http://127.0.0.1:5000/add', json={'title': title})
            print("add_book() started")
            print("add() started")
            data = response.json()
            print(data)
            print("add() completed")
            print("add_book() completed")
        except Exception as e:
            print(e)
            
    def borrow_book(self):
        try:
            title = input("Enter book title\n").lower().strip()
            user = input("Enter borrower\n").lower().strip()
            response = requests.post('http://127.0.0.1:5000/borrow', json={'title': title, 'user': user})
            data = response.json()
            print(data)
        except Exception as e:
            print(e)
            
    def return_book(self):
        try:
            title = input("Enter book title\n").lower().strip()
            response = requests.post('http://127.0.0.1:5000/returns', json={'title': title})
            data = response.json()
            print(data)
        except Exception as e:
            print(e)
            
    def delete_book(self):
        try:
            title = input("Enter book title\n").lower().strip()
            response = requests.post('http://127.0.0.1:5000/delete', json={'title': title})
            data = response.json()
            print(data)
        except Exception as e:
            print(e)

    def display_books(self):
        try:
            response = requests.get('http://127.0.0.1:5000')
            data=response.json()
            df = pd.DataFrame(data['data'])
            print(df)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    try:
        cli = LibraryCLI()
        cli.run()
    except Exception as e:
            print(e)
