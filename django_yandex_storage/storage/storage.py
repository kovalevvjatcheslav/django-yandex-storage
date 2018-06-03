from django.core.files.storage import Storage
from django.conf import settings
from yadiskapi.yadiskapi import Disk
import warnings
from django.utils.deprecation import RemovedInDjango20Warning
import requests

class YandexStorageException(Exception):
    pass

class YandexStorage(Storage):
    def __init__(self, options=None):
        if not options:
            options = settings.YANDEXSTORAGE_CONFIG
        self.disk = Disk(options.get('token'))

    @property
    def _get_files(self):
        """Возвращает список файлов в хранилище"""
        return [item['name'] for item in self.disk.get_files()['items']]

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
        self.disk.delete_resources('app:/{}'.format(name))

    def exists(self, name):
        """
        Returns True if a file referenced by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
        return name in self._get_files

    def listdir(self, path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first item being directories, the second item being files.
        """
        res = ([], [])
        for i in self.disk.get_resources_metainfo('app:/{}'.format(path))['_embedded']['items']:
            if i['type'] == 'dir':
                res[0].append(i['name'])
            else:
                res[1].append(i['name'])
        return res

    def size(self, name):
        """
        Returns the total size, in bytes, of the file specified by name.
        """
        raise NotImplementedError('subclasses of Storage must provide a size() method')

    def url(self, name):
        """
        Returns an absolute URL where the file's contents can be accessed
        directly by a Web browser.
        """
        raise NotImplementedError('subclasses of Storage must provide a url() method')

    def accessed_time(self, name):
        """
        Returns the last accessed time (as datetime object) of the file
        specified by name. Deprecated: use get_accessed_time() instead.
        """
        warnings.warn(
            'Storage.accessed_time() is deprecated in favor of get_accessed_time().',
            RemovedInDjango20Warning,
            stacklevel=2,
        )
        raise NotImplementedError('subclasses of Storage must provide an accessed_time() method')

    def created_time(self, name):
        """
        Returns the creation time (as datetime object) of the file
        specified by name. Deprecated: use get_created_time() instead.
        """
        warnings.warn(
            'Storage.created_time() is deprecated in favor of get_created_time().',
            RemovedInDjango20Warning,
            stacklevel=2,
        )
        raise NotImplementedError('subclasses of Storage must provide a created_time() method')

    def modified_time(self, name):
        """
        Returns the last modified time (as datetime object) of the file
        specified by name. Deprecated: use get_modified_time() instead.
        """
        warnings.warn(
            'Storage.modified_time() is deprecated in favor of get_modified_time().',
            RemovedInDjango20Warning,
            stacklevel=2,
        )
        raise NotImplementedError('subclasses of Storage must provide a modified_time() method')

    def _save(self, name, content):
        content.open()
        upload_path = self.disk.upload('app:/{}'.format(name))['href']
        response = requests.put(upload_path, content.read())
        if response.status_code not in [201, 202]:
            raise YandexStorageException(response.status_code)
        content.close()
        return name

