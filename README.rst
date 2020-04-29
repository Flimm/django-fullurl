.. image:: https://img.shields.io/pypi/v/django-fullurl.svg
    :target: https://pypi.org/project/django-fullurl/
    :alt: django-fullurl on PyPI

.. image:: https://img.shields.io/pypi/l/django-fullurl.svg
    :target: https://pypi.org/project/django-fullurl/
    :alt: django-fullurl on PyPI

.. image:: https://img.shields.io/pypi/wheel/django-fullurl.svg
    :target: https://pypi.org/project/django-fullurl/
    :alt: django-fullurl on PyPI

.. image:: https://img.shields.io/pypi/pyversions/django-fullurl.svg
    :target: https://pypi.org/project/django-fullurl/
    :alt: django-fullurl on PyPI

.. image:: https://travis-ci.org/Flimm/django-fullurl.svg?branch=master
    :target: https://travis-ci.org/Flimm/django-fullurl
    :alt: Travis CI for django-fullurl (master branch)

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/Flimm
    :alt: Say Thanks!
    
------

Introduction
=============

**django-fullurl** adds three new template tags to Django: ``fullurl``, ``fullstatic``, and ``buildfullurl``.

``fullurl`` and ``fullstatic`` behave like ``url`` and ``static`` respectively, but they always return an absolute URL with the scheme and authority/domain parts.

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

``buildfullurl`` takes a relative URL as an argument, and prints an absolute URL with the scheme and authority parts. For example:

.. code:: html+django

    {% buildfullurl article.cover.url %}

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

Template tags summary
=====================

- ``{% fullurl "some-url-name" v1 v2 %}`` This behaves like the ``url`` Django template tag (`doc <https://docs.djangoproject.com/en/stable/ref/templates/builtins/#url>`__), but it returns a full URL instead of a relative one.
- ``{% fullstatic "images/hi.jpg" %}`` This behaves like the ``static`` Django template tag (`doc <https://docs.djangoproject.com/en/stable/ref/templates/builtins/#static>`__), but it returns a full URL instead of a relative one.
- ``{% buildfullurl "/foobar" %}`` This will convert a relative URL into a full URL using ``request.build_absolute_uri`` (`doc <https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpRequest.build_absolute_uri>`__).

Example usage
=============

OpenGraph
---------

OpenGraph URLs need to be absolute, including scheme and authority parts. Here's how you can use ``fullurl`` and ``fullstatic`` to help with this:

.. code:: html+django

    {% load fullurl %}
    
    <meta property="og:url" content="{% fullurl "articles:article" article=article %}">
    <meta property="og:image" content="{% fullstatic "cat.jpg" %}">
    

You can convert a URL from relative to absolute using ``buildfullurl`` tag:

.. code:: html+django

    {% load fullurl %}
    
    <meta property="og:url" content="{% buildfullurl article.get_absolute_url %}">
    <meta property="og:image" content="{% buildfullurl article.image.url %}">

Facebook static share link
--------------------------

If you want to create a Facebook share button using a link, you can use the ``sharer.php`` feature. The value for the ``u`` query parameter needs to be an absolute URL, encoded using the ``urlencode`` filter, like this:

.. code:: html+django

   {% load fullurl %}

   <a href="https://www.facebook.com/sharer/sharer.php?u={% filter urlencode %}{% buildfullurl article.get_absolute_url %}{% endfilter %}">
     Share
   </a>
  

See also
========

Here are some alternatives, in alphabetical order:

- `django-absoluteuri <https://pypi.org/project/django-absoluteuri/>`__ (`GitHub <https://github.com/fusionbox/django-absoluteuri>`__, `Django Packages <https://djangopackages.org/packages/p/django-absoluteuri/>`__) provides two template tags: ``absoluteuri`` and ``absolutize``. Unlike this app, it uses the site framework to determine the domain to use, which could be an additional database query. This can be useful in some situations, for instance when creating emails.
- `django-absoluteurl <https://pypi.org/project/django-absoluteurl/>`__ (`GitHub <https://github.com/bgryszko/django-absoluteurl>`__, `Django Packages <https://djangopackages.org/packages/p/django-absoluteurl/>`__) provides a template tag ``absoluteurl`` that works in a similar fashion as ``fullurl``. It does not seem to work in Python 2, or with newer Django versions, however.
- django-full-url (`GitHub <https://github.com/RRMoelker/django-full-url>`__) allows you to get specific parts of the current URL using code like ``{{ url_parts.domain }}``, among other things. It does not provide the same functionality as this app, the naming similarity was unintentional.
- `django-urltags <https://pypi.org/project/django-urltags/>`__ (`Django Packages <https://djangopackages.org/packages/p/django-urltags/>`__) provides a few template tags, including ``absurl``, but it hasn't been updated since 2012 and it doesn't seem to work on recent Django versions.
