from django import template

register = template.Library()

@register.filter
def get_dict_value(dictionary, key):
    return dictionary.get(key, None)



@register.filter
def get_matching_user(data1, email_id):
    # Implement your logic to search for the matching user in data1
    # based on the email_id and return the matching user or None
    matching_user = None
    for user in data1:
        if user.user == email_id:
            matching_user = user
            break
    return matching_user