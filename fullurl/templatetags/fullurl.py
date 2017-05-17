from django import template
from django.template import defaulttags
from django.template.base import Node
from django.templatetags.static import do_static

register = template.Library()

@register.tag
def fullurl(parser, token):
    """Return an absolute URL (including the scheme and domain) matching the
    given view with its parameters.

    This is meant to be identical to the built-in tag `url`, except that it
    always returns an absolute URL with the scheme and authority parts.

    For example, take this `url` tag:

        {% url "articles:article" slug="hello" %}

    This could return:

        /articles/hello

    This is considered an absolute URL because it begins with a forward-slash,
    however, it is not an absolute absolute URL, because it does not include
    the scheme and authority parts.

    Compare with this `fullurl` tag:

        {% fullurl "articles:article" slug="hello" %}

    This returns:

        http://example.com/articles/hello

    """
    return FullURLNode(defaulttags.url(parser, token))


@register.tag
def fullstatic(parser, token):
    return FullStaticNode(do_static(parser, token))


@register.simple_tag(takes_context=True)
def buildfullurl(context, url):
    """Converts relative URL to absolute.

    For example:

        {% buildfullurl article.get_absolute_url %}

    or:

        {% buildfullurl "/custom-url/" %}

    """
    return context.request.build_absolute_uri(url)


class FullURLNode(Node):
    def __init__(self, subject):
        self._subject = subject

    def render(self, context):
        url = self._subject.render(context)
        return context.request.build_absolute_uri(url)

class FullStaticNode(Node):
    def __init__(self, subject):
        self._subject = subject

    def render(self, context):
        url = self._subject.render(context)
        return context.request.build_absolute_uri(url)
