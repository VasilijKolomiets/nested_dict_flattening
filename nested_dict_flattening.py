"""
    This module gives  function(s) for nested dict flattening (by some pattern).

    It may be useful in some socisl networks parsing

"""

def flatten_by_pattern(dict_in: dict, pattern_dict: dict) -> dict:
    """Flatten the 'dict_in' nested dict with some pattern dictionary - 'pattern_dict'.

    Args:
        dict_in (dict): income (nested) dictionary
        pattern_dict (dict): pattern dict for flattening

    Returns:
        dict: Flatten dictionary
    """
    return dict() 

if __name__ == '__main__':
    if isinstance(flatten_by_pattern(dict(), dict()), dict):
        print("Вона працює!")