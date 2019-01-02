import requests as req
import time


from kegg_data_type import KOID
from kegg_data_type import RID


def get_rid_from_kid(ko_id):
    time.sleep(5)
    k_id = ""
    r_id_list = list()
    url = r'http://rest.kegg.jp/link/reaction/ko:{}'.format(ko_id)
    response = req.get(url)
    if "R0" in response.text:
        for line in response.text.splitlines():
            tmp = line.split()
            k_id = tmp[0].split(":")[-1].strip()
            r_id = tmp[1].split(":")[-1].strip()
            r_id_list.append(r_id)
        res = KOID(kid=k_id, rid_list=r_id_list)
        return res
    else:
        print("{} has No reaction data!".format(ko_id))
        return False


def get_cid_from_rid(kid, rid):
    time.sleep(5)
    url = r'http://rest.kegg.jp/get/{}'.format(rid)
    response = req.get(url)
    cid_list = list()
    name = ""
    # definition
    defnt = ""
    # equation
    eqt = ""
    if "C0" in response.text:
        for line in response.text.splitlines():
            if "NAME" in line:
                name = " ".join(line.split()[1:])
            if "DEFINITION" in line:
                defnt = " ".join(line.split()[1:])
            if "EQUATION" in line:
                eqt = " ".join(line.split()[1:])
                tmp = line.split()
                for i in tmp:
                    if "C" in i:
                        cid_list.append(i)

    res = RID(kid=kid, cid_list=cid_list, rid_eq=eqt, rid_def=defnt, rid=rid)
    return res
