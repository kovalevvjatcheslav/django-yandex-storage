from unittest import main, TestCase
from django_yandex_storage.storage.storage import YandexStorage
from settings import TOKEN
from contextlib import contextmanager
from django.core.files.base import ContentFile
from django.conf import settings

settings.configure()


class TestYandexStorage(TestCase):
    def setUp(self):
        self.storage = YandexStorage(options={'token': TOKEN})

    @contextmanager
    def assertNotRaises(self, funct_name, exception, prepare=None, fin=None):
        if prepare:
            for func, params in prepare.items():
                func(*params)
        try:
            yield None
        except exception as e:
            raise self.failureException('Ошибка при вызове функции: {}, {}'.format(funct_name, e))
        finally:
            if fin:
                for func, params in fin.items():
                    func(*params)

    def test_get_files(self):
        with self.assertNotRaises('_get_files', Exception):
            print(self.storage._get_files)

    def test_exists(self):
        with self.assertNotRaises('exists', Exception):
            if self.storage._get_files:
                self.storage.exists(self.storage._get_files[0])

    def test_save(self):
        with self.assertNotRaises('save', Exception):
            out = ContentFile('test\n', 'test.txt')
            name = self.storage.save('test.txt', out)
            self.storage.delete(name)

    def test_listdir(self):
        with self.assertNotRaises('listdir', Exception):
            self.storage.listdir('')

    def test_size(self):
        with self.assertNotRaises('size', Exception):
            out = ContentFile('test\n', 'test.txt')
            name = self.storage.save('test.txt', out)
            self.storage.size('test.txt')
            self.storage.delete(name)

    def test_get_accessed_time(self):
        with self.assertNotRaises('get_accessed_time', Exception):
            self.storage.get_accessed_time(self.storage._get_files[0])

    def test_get_created_time(self):
        with self.assertNotRaises('get_created_time', Exception):
            self.storage.get_created_time(self.storage._get_files[0])

    def test_get_modified_time(self):
        with self.assertNotRaises('get_modified_time', Exception):
            self.storage.get_modified_time(self.storage._get_files[0])


if __name__ == '__main__':
    main()
