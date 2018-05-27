from unittest import main, TestCase
from django_yandex_storage.storage.storage import YandexStorage
from settings import TOKEN

class TestYandexStorage(TestCase):
    def setUp(self):
        self.storage = YandexStorage(options={'token': TOKEN})

