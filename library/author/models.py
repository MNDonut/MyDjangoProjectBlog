from django.db import models, IntegrityError, DataError
from django.forms.models import model_to_dict


class Author(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes last name of the author
        type surname: str max_length=20
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=20

    """
    name = models.CharField(max_length=20, default="")
    surname = models.CharField(max_length=20, default="")
    patronymic = models.CharField(max_length=20, default="")


    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        return f"'id': {self.id}, 'name': '{self.name}', 'surname': '{self.surname}', 'patronymic': '{self.patronymic}'"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """
        return f"Author(id={self.id})"


    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        return Author.objects.get(id=author_id) if Author.objects.filter(id=author_id).exists() else None

    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        return True if Author.objects.filter(id=author_id).exists() and \
                    Author.objects.filter(id = author_id).delete() else False



    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: a new author object which is also written into the DB
        """
        forSave = Author(name=name, surname=surname, patronymic=patronymic)
        forSave.save()
        return forSave if len(name) < 20 and len(surname) < 20 and len(patronymic) < 20 else None



    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """
        return model_to_dict(self)


    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates author in the database with the specified parameters.\n
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: None
        """
        name = self.name if name == None else name
        surname = self.surname if surname == None else surname
        patronymic = self.patronymic if patronymic == None else patronymic
        Author.objects.filter(id = self.id).update(name = name, surname = surname, patronymic = patronymic) \
                            if len(name) < 20 and len(surname) < 20 and len(patronymic) < 20 else None
        return None



    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        return Author.objects.all()

