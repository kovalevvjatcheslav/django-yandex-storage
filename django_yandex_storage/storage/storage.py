from django.core.files.storage import Storage
from django.conf import settings
from yadiskapi.yadiskapi import Disk
import warnings
from django.utils.deprecation import RemovedInDjango20Warning
from django.core.files import File, locks


class YandexStorage(Storage):
    def __init__(self, options=None):
        if not options:
            options = settings.YANDEXSTORAGE_CONFIG
        self.disk = Disk(options.get('token'))

    def path(self, name):
        """
        Returns a local filesystem path where the file can be retrieved using
        Python's built-in open() function. Storage systems that can't be
        accessed using open() should *not* implement this method.
        """
        raise NotImplementedError("This backend doesn't support absolute paths.")

    def delete(self, name):
        """
        Deletes the specified file from the storage system.
        """
        raise NotImplementedError('subclasses of Storage must provide a delete() method')

    def exists(self, name):
        """
        Returns True if a file referenced by the given name already exists in the
        storage system, or False if the name is available for a new file.
        """
        raise NotImplementedError('subclasses of Storage must provide an exists() method')

    def listdir(self, path):
        """
        Lists the contents of the specified path, returning a 2-tuple of lists;
        the first item being directories, the second item being files.
        """
        raise NotImplementedError('subclasses of Storage must provide a listdir() method')

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

