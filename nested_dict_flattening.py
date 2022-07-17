"""
    This module gives  function(s) for nested dict flattening (by some pattern).

    It may be useful in some socisl networks parsing

    Development 4-th step. Recursive calls.
    Development 5-th step. Composite output keys.

"""
from datetime import datetime as dt


def flatten_by_pattern(dict_in: dict, pattern_dict: dict, parent_key='') -> dict:
    """Flatten the 'dict_in' nested dict with some pattern dictionary - 'pattern_dict'.

    Args:
        dict_in (dict): income (nested) dictionary
        pattern_dict (dict): pattern dict for flattening

    Returns:
        dict: Flatten dictionary
    """
    out_dict = dict()
    for key, value in pattern_dict.items():
        if key in dict_in:
            current_composite_key = parent_key + '.' + key
            print(F'{key=} {dict_in[key]=}')
            if value is True:                       # copying proper final value
                out_dict.update({current_composite_key: dict_in[key]})
            elif callable(value):
                out_dict.update({current_composite_key: value(dict_in[key])})
            elif isinstance(value, dict):
                out_dict.update(flatten_by_pattern(dict_in[key], value, current_composite_key))
            else:
                assert False, F'What the "{value}"? Or "True" or dict !! '

    return out_dict


if __name__ == '__main__':
    nested_dict_example = dict(
        bdate='11.7.1993',
        last_name='Kovalenko',
        first_name='Shimon',
        city=dict(id='3', title='Moscow'),
        country=dict(id='77', title='Russia'),
        schools=dict(id='378', year_from='2000', year_to='2012', name='School 33'),
        last_seen=dict(time=1658061885.242944),
        universities=dict(
            id='719',  name='MSU',
            faculty='Applied Mathematics',
            graduation=dict(year_from='2013', year_to='2018'),
        )
    )

    flatten_pattern_dict = dict(
        bdate=True,
        last_name=True,
        first_name=True,
        city=dict(title=True),
        country=dict(title=True),
        schools=dict(year_to=int),
        last_seen=dict(time=dt.fromtimestamp),
        universities=dict(
            name=True,
            graduation=dict(year_to=int),
        ),
    )

    print(flatten_by_pattern(nested_dict_example, flatten_pattern_dict))
