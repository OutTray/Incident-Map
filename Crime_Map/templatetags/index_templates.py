from django import template
register = template.Library()

@register.simple_tag
def get_number_entries(button_information, id):
    for i in range(len(button_information)):
        if button_information[i][0] == id:
            return button_information[i][2]

