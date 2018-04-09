#  -- coding: utf8 --
__author__ = 'esokur'

import sqlite3 as mdb
import re

from translator_corpus.settings import DATABASES

NAME = DATABASES['default']['NAME']


def regexp(y, x, search=re.search):
    return 1 if search(y, x) else 0


class Database(object):
    """Класс для общения с базой данных MySQL"""
    
    def __init__(self):
        """Создать соединение с базой данных.

        В параметрах соединения указывается хост, логин, пароль, название базы данных, кодировка.
        """
        self._connection = mdb.connect(NAME)

    def commit(self):
        self._connection.commit()

    def execute(self, q):
        """Вернуть результат выполнения запроса в виде массива кортежей.

        Каждый кортеж - строка базы данных, сформированная по запросу.
        """
        self.cur = self._connection.cursor()  # mdb.cursors.DictCursor
        self._connection.create_function('regexp', 2, regexp)
        self.cur.execute(q)
        res = self.cur.fetchall()
        self.cur.close()
        return res
