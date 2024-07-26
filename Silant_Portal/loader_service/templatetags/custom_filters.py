from django import template

register = template.Library()


@register.filter()
def roles_translator(role):
    ROLES = [
        ('CL', 'Клиент'),
        ('SR', 'Сервисная организация'),
        ('MG', 'Менеджер'),
    ]
    for r in ROLES:
        if role == r[0]:
            translated_role = r[1]

    return translated_role