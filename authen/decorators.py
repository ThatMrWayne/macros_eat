

def set_custom_attr(attr_name, attr_value):
    def decorator(func):
        setattr(func, attr_name, attr_value)
        return func
    return decorator
