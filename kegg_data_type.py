from collections import OrderedDict
from typing import NamedTuple


class KOID(NamedTuple):
    kid: str
    rid_list: list
    #key organ value : entry
    organism_dict: OrderedDict


class RID(NamedTuple):
    kid: str
    rid: str
    rid_eq: str
    rid_def: str
    cid_list: list
