from django import template

register = template.Library()

@register.filter
def has_menu_url(menu_queryset, url_to_check):
    return menu_queryset.filter(url=url_to_check).exists()
