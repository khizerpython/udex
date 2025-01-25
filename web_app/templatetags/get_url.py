from django import template
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from web_app.constants import DEFAULT_404_URL

import os

register = template.Library()


@register.simple_tag
def get_url_against_urlname(urlname):
    try:
        return reverse(urlname)
    except NoReverseMatch:
        return DEFAULT_404_URL

@register.simple_tag
def email_page_domain():
    return os.environ.get("EMAIL_PAGE_DOMAIN", default="http://localhost:8000")

