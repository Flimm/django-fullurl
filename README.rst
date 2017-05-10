.. image:: https://img.shields.io/pypi/v/django-fullurl.svg
    :target: https://pypi.python.org/pypi/django-fullurl

.. image:: https://img.shields.io/pypi/l/django-fullurl.svg
    :target: https://pypi.python.org/pypi/django-fullurl

.. image:: https://img.shields.io/pypi/wheel/django-fullurl.svg
    :target: https://pypi.python.org/pypi/django-fullurl

.. image:: https://img.shields.io/pypi/pyversions/django-fullurl.svg
    :target: https://pypi.python.org/pypi/django-fullurl

.. image:: https://travis-ci.org/Flimm/django-fullurl.svg?branch=master
    :target: https://travis-ci.org/Flimm/django-fullurl

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/Flimm
    
------

Introduction
=============

**django-fullurl** adds two new template tags: ``fullurl`` and ``fullstatic``. They behave like ``url`` and ``static`` respectively, but they always return an absolute URL with the scheme and authority/domain parts.

For example, take this ``url`` tag:

.. code:: html+django

   {% url "articles:article" slug="hello" %}
   
In our example, this prints::

    /articles/hello
    
This is called by some an absolute URL, because it begins with a forward-slash. However, it is not an *absolute* absolute URL, because it does not contain the scheme and authority parts.

If we replace ``url`` with ``fullurl``, it will print this result::

    http://example.com/articles/hello
    
Behind the scenes, it uses `request.build_absolute_uri <https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpRequest.build_absolute_uri>`__ to determine the correct scheme and authority/domain parts.

In the same way that ``fullurl`` extends ``url``, ``fullstatic`` extends the ``static`` template tag.

Installation
============

Run on the command-line::

    $ pip install django-fullurl
    
Make sure these two apps are included in your ``INSTALLED_APPS`` settings:

.. code:: python

    INSTALLED_APPS = [
        'django.contrib.staticfiles',
        'fullurl',
        # ...
    ]
    
Make sure ``django.template.context_processors.request`` is included in your context processors.

Example usage
=============

OpenGraph URLs need to be absolute, including scheme and authority parts. Here's how you can use ``fullurl`` and ``fullstatic`` to help with this:

.. code:: html+django

    {% load fullurl %}
    
    <meta property="og:url" content="{% fullurl "articles:article" article=article %}">
    <meta property="og:image" content="{% fullstatic "cat.jpg" %}">
    

Alternatively you can convert URL from relative to absolute using ``build_fullurl`` tag:

.. code:: html+django

    {% build_fullurl article.get_absolute_url %}
    {% build_fullurl "/custom-url/" %}


Or with sorl-thumbnail:

.. code:: html+django

    {% thumbnail article.image as thumb %}
    {% build_fullurl thumb.url %}
    {% endthumbnail %}

See also
========

Here are some alternatives, in alphabetical order:

- `django-absoluteuri <https://pypi.python.org/pypi/django-absoluteuri>`__ (`GitHub <https://github.com/fusionbox/django-absoluteuri>`__, `Django Packages <https://djangopackages.org/packages/p/django-absoluteuri/>`__) provides two template tags: ``absoluteuri`` and ``absolutize``. Unlike this app, it uses the site framework to determine the domain to use, which could be an additional database query. This can be useful in some situations, for instance when creating emails.
- `django-absoluteurl <https://pypi.python.org/pypi/django-absoluteurl>`__ (`GitHub <https://github.com/bgryszko/django-absoluteurl>`__, `Django Packages <https://djangopackages.org/packages/p/django-absoluteurl/>`__) provides a template tag ``absoluteurl`` that works in a similar fashion as ``fullurl``. It does not seem to work in Python 2, or with newer Django versions, however.
- django-full-url (`GitHub <https://github.com/RRMoelker/django-full-url>`__) allows you to get specific parts of the current URL using code like ``{{ url_parts.domain }}``, among other things. It does not provide the same functionality as this app, the naming similarity was unintentional.
- `django-urltags <https://pypi.python.org/pypi/django-urltags>`__ (`Django Packages <https://djangopackages.org/packages/p/django-urltags/>`__) provides a few template tags, including ``absurl``, but it hasn't been updated since 2012 and it doesn't seem to work on recent Django versions.
