# nested_dict_flattening

    This module gives  function(s) for nested dict flattening (by some pattern).

    It may be useful in some socisl networks parsing
    
#### Step 1.  Starting code
#### Step 2.  Code with example of nested dict printing out.
#### Step 3.  1-st attempt to form resulting dictionary. All keys presence assumed.

```Python
"""
    This module gives  function(s) for nested dict flattening (by some pattern).

    It may be useful in some socisl networks parsing

    Development step 3. 1-st attempt to form resulting dictionary. All keys presence assumed.
"""


def flatten_by_pattern(dict_in: dict, pattern_dict: dict) -> dict:
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
            print(F'{key=} {dict_in[key]=}')
            if value is True:                       # copyting proper final value
                out_dict.update({key: dict_in[key]})

    return out_dict


if __name__ == '__main__':
    nested_dict_example = dict(
        bdate='11.7.1993',
        last_name='Kovalenko',
        first_name='Shimon',
        city=dict(id=3, title='Moscow'),
        country=dict(id=77, title='Russia'),
        schools=dict(id=378, year_from=2000, year_to=2012, name='School 33'),
        last_seen=dict(time=True),
        universities=dict(
            id=719,  name='MSU',
            faculty='Applied Mathematics',
            graduation=dict(year_from=2013, year_to=2018),
        )
    )

    flatten_pattern_dict = dict(
        bdate=True,
        last_name=True,
        first_name=True,
        city=dict(title=True),
        country=dict(title=True),
        schools=dict(year_to=True),
        last_seen=dict(time=True),
        universities=dict(
            name=True,
            graduation=dict(year_to=True),
        ),
    )

    print(flatten_by_pattern(nested_dict_example, flatten_pattern_dict))
```

The problem is - we have formed out only keys lelel 1 of input dictionary.     
May be try recursion?

