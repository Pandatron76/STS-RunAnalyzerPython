import collections


def flatten_dict_by_floor(card, floor_picked_dict):
    current_floor_picks = []
    for k, v in floor_picked_dict.items():
        if int(k) == int(card.floor):
            current_floor_picks.append(v)

    current_floor_picks.append(card.picked)
    flatten_picks = flatten_word_list(current_floor_picks)
    floor_picked_dict.update({int(round(card.floor)): flatten_picks})

    return floor_picked_dict


def flatten_word_list(x):
    result = []
    for el in x:
        if isinstance(x, collections.Iterable) and not isinstance(el, str):
            result.extend(flatten_word_list(el))
        else:
            result.append(el)

    return result
