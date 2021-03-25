from django.db import models, DataError, IntegrityError

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
import datetime


class Order(models.Model):


    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """


    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'
    def to_dict(self):

        pass

    @staticmethod
    def create(user, book, plated_end_at):
        pass


    @staticmethod
    def get_by_id(order_id):
        pass


    def update(self, plated_end_at=None, end_at=None):
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def get_not_returned_books():
        pass

    @staticmethod
    def delete_by_id(order_id):
        pass