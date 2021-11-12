import mysql.connector
from mysql.connector.cursor_cext import CMySQLCursor

from extensions.singleton import Singleton
from models.user import User


class Database(metaclass=Singleton):
    def __init__(self):
        self.connection = mysql.connector.connect(user='artyom', password='inmate4859',
                                                  host='localhost', database='kursach_db')

    def close_connection(self):
        self.connection.close()
        self.connection = None

    def create_user(self, username, password):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc('add_user', [username, password])
            self.connection.commit()
        except mysql.connector.Error as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def login_user(self, username, password):
        cursor = None
        try:
            cursor = self.connection.cursor()
            username_out = ""
            is_staff_out = ""
            id_out = ""
            args = cursor.callproc('login_user', [username, password, username_out, is_staff_out, id_out])
            self.connection.commit()
            if args[2] is not None:
                return User(username=args[2], is_staff=args[3], id=args[4])
        except mysql.connector.Error as e:
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_all_cars(self) -> CMySQLCursor.stored_results:
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc('get_all_cars')
            self.connection.commit()
            return cursor.stored_results()
        except mysql.connector.Error as e:
            # TODO: error log
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_cars_by_name(self, name):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc('get_cars_by_name', [name])
            self.connection.commit()
            return cursor.stored_results()
        except mysql.connector.Error as e:
            # TODO: error log
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_all_dealerships(self):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc('get_all_dealerships')
            self.connection.commit()
            return cursor.stored_results()
        except mysql.connector.Error as e:
            # TODO: error log
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def get_all_orders(self, client_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc('get_orders_by_clientID', [client_id])
            self.connection.commit()
            return cursor.stored_results()
        except mysql.connector.Error as e:
            # TODO: error log
            print(e)
        finally:
            if cursor is not None:
                cursor.close()

    def add_order(self, days, count, client_id, car_id):
        cursor = None
        try:
            cursor = self.connection.cursor()
            cursor.callproc('add_order', [days, count, client_id, car_id])
            self.connection.commit()
        except mysql.connector.Error as e:
            # TODO: error log
            print(e)
        finally:
            if cursor is not None:
                cursor.close()
