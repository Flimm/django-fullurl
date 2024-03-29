from django.test import TestCase
from django.test.client import RequestFactory
from django.template import Template, RequestContext
import django

if django.VERSION < (3, 2):
    from django.conf.urls import url as re_path
else:
    from django.urls import re_path

urlpatterns = [
    re_path(r'^foobar$', lambda r: None, name='example'),
    re_path(r'^foobar/(.+)$', lambda r: None, name='example2'),
    re_path(r'^foobar/(?P<slug>.+)$', lambda r: None, name='example3'),
]

class FullURLTestCase(TestCase):
    TEMPLATE = Template('{% load fullurl %}{% fullstatic "hello" }')

    def setUp(self):
        factory = RequestFactory()
        request = factory.get('/')
        self.request_context = RequestContext(request, {})

    def test_fullstatic(self):
        template = Template('{% load fullurl %}{% fullstatic "one/two/hello.jpg" %}')
        rendered = template.render(self.request_context)
        self.assertEqual(rendered, 'http://testserver/static/one/two/hello.jpg')

    def test_fullstatic_with_external_domain(self):
        template = Template('{% load fullurl %}{% fullstatic "one/two/hello.jpg" %}')
        with self.settings(STATIC_URL='http://example.com/static/'):
            rendered = template.render(self.request_context)
            self.assertEqual(rendered, 'http://example.com/static/one/two/hello.jpg')

    def test_fullurl(self):
        template = Template('{% load fullurl %}{% fullurl "example" %}')
        with self.settings(ROOT_URLCONF=__name__):
            rendered = template.render(self.request_context)
            self.assertEqual(rendered, 'http://testserver/foobar')

    def test_fullurl_with_args(self):
        template = Template('{% load fullurl %}{% fullurl "example2" "welcome" %}')
        with self.settings(ROOT_URLCONF=__name__):
            rendered = template.render(self.request_context)
            self.assertEqual(rendered, 'http://testserver/foobar/welcome')

    def test_fullurl_with_kwargs(self):
        template = Template('{% load fullurl %}{% fullurl "example3" slug="welcome" %}')
        with self.settings(ROOT_URLCONF=__name__):
            rendered = template.render(self.request_context)
            self.assertEqual(rendered, 'http://testserver/foobar/welcome')

    def test_buildfullurl_custom(self):
        template = Template('{% load fullurl %}{% buildfullurl "/custom-url/" %}')
        rendered = template.render(self.request_context)
        self.assertEqual(rendered, 'http://testserver/custom-url/')
