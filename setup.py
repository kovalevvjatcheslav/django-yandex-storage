from setuptools import setup, find_packages

with open('README.md', mode='r') as readme:
    README = readme.read()

setup(
    name='django-yandex-storage',
    license='GNU LGPLv3',
    description='Пакет реализует хранилище на базе яндекс диска.',
    long_description=README,
    url='https://github.com/kovalevvjatcheslav/django-yandex-storage',
    author='Ковалев Вячеслав',
    author_email='kovalevvjatcheslav@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU LGPLv3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
