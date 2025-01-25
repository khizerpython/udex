from django import template
import uuid
register = template.Library()

@register.filter
def is_string(val):
    return isinstance(val, str)

@register.filter
def apply_style_on_p(value):
    if isinstance(value, str):
        return value.replace("<p>","<p style='display:inline;'>")
    elif isinstance(value, list):
        return ", ".join(value)
    
    return value

@register.filter
def get_key(dictionary, key):
    return dictionary.get(key)


@register.filter
def is_uuid(value):
    
    try:
        uuid.UUID(value)
        return True
    except (ValueError, TypeError):
        return False