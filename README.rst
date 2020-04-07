MoWAKi - Python utilities
#########################

This package provides several common utilities for MoWAKi_ apps.

.. _MoWAKi: https://www.mowaki.org


.. image:: https://travis-ci.org/rshk/mowaki-py.svg?branch=master
    :target: https://travis-ci.org/rshk/mowaki-py


Storage
=======

Provides a common abstraction for file storage.

Currently supports storing data in:

- memory (mostly for testing)
- local filesystem (mostly for local development)
- s3 buckets


.. code-block:: python

   from mowaki.storage import get_storage_from_url

   storage = get_storage_from_url('s3://bucket/key-prefix')
   # storage = get_storage_from_url('file:///path/to/files')

   storage.put_file('hello.txt', b'Hello world!')
   data = storage.get_file_content('hello.txt')
   assert data == b'Hello world!'


Authentication
==============

Issue and validate JWT tokens:


.. code-block:: python

   from mowaki.auth import TokenMaker

   tm = TokenMaker(SECRET_KEY, issuer='x', audience='login')

   token = tm.issue(subject='foobar')
   data = tm.validate(token)
   assert data['subject'] == 'foobar'



Config
======

Convenience functions for loading configuration from environment variables:


.. code-block:: python

    import os
    from mowaki.config import Config


    class AppConfig(Config):
        SECRET_KEY: str
        DATABASE_URL: str
        ENABLE_FEATURE_1: bool = False


    cfg = AppConfig(os.environ)

    # Access loaded configuration
    cfg.SECRET_KEY
