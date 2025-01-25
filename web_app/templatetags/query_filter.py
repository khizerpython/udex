from django import template
from django.db.models.functions import Cast
from django.db.models import TextField

register = template.Library()

@register.filter(name='get_value_in_qs')
def get_value_in_qs(queryset, key):
    return queryset.values(key, flat=True)

@register.filter(name='get_value_list_in_qs')
def get_value_list_in_qs(queryset, key_cast):
    splitted_str = key_cast.split(",")
    key = splitted_str[0]
    cast = bool(splitted_str[1]) if len(splitted_str) == 2 else False
    if cast:
        try:
            _filtered_uuids =  queryset.annotate(str_id=Cast(key, output_field=TextField())).values_list("str_id", flat=True)
        except ValueError:
            _filtered_uuids =  queryset.values_list("str_id", flat=True)
        
        return list(_filtered_uuids)

    _filtered_uuids =  queryset.values_list(key, flat=True)
    return [str(uuid) for uuid in _filtered_uuids]
    