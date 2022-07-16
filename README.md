# Nested dicticonary flattening.

    This module gives  function(s) for nested dict flattening (by some pattern).

    It may be useful in some socisl networks parsing    
    
#### Step 0.  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet   
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
The final prints produce:
```
{'bdate': '11.7.1993', 'last_name': 'Kovalenko', 'first_name': 'Shimon'}
```


The problem is - we have formed out only keys lelel 1 of input dictionary. 
May be try recursion?

#### Step 4.  Recursion works

Only some lines was added

```Python
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
            if value is True:                       # copying proper final value
                out_dict.update({key: dict_in[key]})
            elif isinstance(value, dict):
                out_dict.update(flatten_by_pattern(dict_in[key], value))
            else:
                assert False, F'What the "{value}"? Or "True" or dict !! '

    return out_dict

```

It gives the last print  output:
```
{'bdate': '11.7.1993', 'last_name': 'Kovalenko', 'first_name': 'Shimon', 'title': 'Russia', 'year_to': 2018, 'time': True, 'name': 'MSU'}
```

It seams all is Ok, but..      
The problem is - we lost fields with identicaly nemes in last dictionary level. We have subkey 'title'  in dictionaries 'city'  &   'country'.
May be try form composed keyfor such situations?

```Python
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
            print(F'{key=} {dict_in[key]=}')
            if value is True:                       # copying proper final value
                out_dict.update({parent_key + '.' + key: dict_in[key]})
            elif isinstance(value, dict):
                out_dict.update(flatten_by_pattern(dict_in[key], value, parent_key=parent_key + '.' + key))
            else:
                assert False, F'What the "{value}"? Or "True" or dict !! '

    return out_dict
```
It gives the last print  output:
```
{'bdate': '11.7.1993', 'last_name': 'Kovalenko', 'first_name': 'Shimon', 'title': 'Russia', 'year_to': 2018, 'time': True, 'name': 'MSU'}
```

It seams much better..      
But it is look like robotic history - not human friendly? isn it?
May be exchange tjese keys to human like?


