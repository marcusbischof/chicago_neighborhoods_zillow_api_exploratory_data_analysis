################################################################
#
# Functions that we may re-use in this exploration.
#
################################################################

import collections

# Code used from: https://stackoverflow.com/a/10076823/6169225
# StackOverflow user who developed this: K3---rnc
def etree_to_dict(t):
    """ This returns a dictionary from an object (= ET.fromstring(response.read().decode())). """
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = collections.defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d
