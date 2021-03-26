from django.db import models, DataError, IntegrityError
from django.core.exceptions import ValidationError
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
import datetime


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField(null=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        end_at = f"'{self.end_at}'" if self.end_at else None
        message = (
            f"'id': {self.id}, "
            f"'user': {self.user.__repr__()}, "
            f"'book': {self.book.__repr__()}, "
            f"'created_at': '{self.created_at}', "
            f"'end_at': {end_at}, "
            f"'plated_end_at': '{self.plated_end_at}'"
        )
        return message

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):

        return {
            'id': self.id,
            'user': self.user,
            'book': self.book,
            'created_at': str(self.created_at),
            'end_at': str(self.end_at) if self.end_at else self.end_at,
            'plated_end_at': str(self.plated_end_at)
        }

    @staticmethod
    def create(user, book, plated_end_at):
        if book.count <= len([order for order in Order.get_not_returned_books() if order.book.id == book.id]):
            return None
        if user.id is None:
            return None
        new_order = Order(user=user, book=book, plated_end_at=plated_end_at)
        try:
            new_order.save()
            return new_order
        except (IntegrityError, AttributeError, DataError, ValueError):
            return None

    @staticmethod
    def get_by_id(order_id):
        try:
            user = Order.objects.get(id=order_id)
            return user
        except Order.DoesNotExist:
            return None

    def update(self, plated_end_at=None, end_at=None):
        if plated_end_at:
            self.plated_end_at = plated_end_at
        if end_at:
            self.end_at = end_at
        self.save()

    @staticmethod
    def get_all():
        all_order = list(Order.objects.all())
        return all_order

    @staticmethod
    def get_not_returned_books():
        orders = [order for order in Order.get_all() if order.end_at is None]
        return orders

    @staticmethod
    def delete_by_id(order_id):
        try:
            user = Order.objects.get(id=order_id)
            user.delete()
            return True
        except Order.DoesNotExist:
            return False
