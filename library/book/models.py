from django.db import models, IntegrityError, DataError
from django.forms.models import model_to_dict

from author.models import Author


class Book(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
    """
    name = models.CharField(max_length=128, default="")
    description = models.TextField(default="")
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField(Author)



    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        authors_list = (
            '[' + ','.join(str(item.id) for item in self.authors.all()) + ']'
            )
        return (
            f"'id': {self.id}, 'name': '{self.name}',"
            f" 'description': '{self.description}', 'count': {self.count},"
            f" 'authors': {authors_list}"
        )

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f"Book(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        """
        :param book_id: SERIAL: the id of a Book to be found in the DB
        :return: book object or None if a book with such ID does not exist
        """
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id).exists() else None

    @staticmethod
    def delete_by_id(book_id):
        """
        :param book_id: an id of a book to be deleted
        :type book_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        return True if Book.objects.filter(id=book_id).exists() and Book.objects.filter(id=book_id).delete() else False



    @staticmethod
    def create(name, description, count=10, authors=None):
        """
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
        :return: a new book object which is also written into the DB
        """
        forSave = Book(name = name, description = "" if not description else description, count = count)
        forSave.save()
        forSave.authors.set([]) if not authors else forSave.authors.set(authors) 
        return forSave if len(name) <= 128 else None


    def to_dict(self):
        """
        :return: book id, book name, book description, book count, book authors
        :Example:
        | {
        |   'id': 8,
        |   'name': 'django book',
        |   'description': 'bla bla bla',
        |   'count': 10',
        |   'authors': []
        | }
        """
        return model_to_dict(self)



    def update(self, name=None, description=None, count=None):
        """
        Updates book in the database with the specified parameters.\n
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        :return: None
        """
        name = self.name if not name else name
        description = self.description if not description else description
        count = self.count if not count else count
        Book.objects.filter(id = self.id).update(name = name, description = description, count = count)
        return None



    def add_authors(self, authors):
        """
        Add  authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        self.authors.add(*set(authors))
        return None



    def remove_authors(self, authors):
        """
        Remove authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        for aut in authors:
            self.authors.remove(aut)
        return None


    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        return list(Book.objects.all())

