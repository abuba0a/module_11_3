from pprint import pprint

x = {}


def introspection_info(obj):
    x['type'] = type(obj)
    x['attributes'] = [method for method in dir(obj) if not callable(getattr(obj, method))]
    x['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    x['module'] = obj.__class__.__module__

    return x


number_info = introspection_info(42)
pprint(number_info)
print()
str_info = introspection_info('apple')
pprint(str_info)
