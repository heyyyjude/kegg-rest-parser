from kegg_parser import get_cid_from_rid
from kegg_parser import get_rid_from_kid


def main(ko_id):
    koid_namedtuple = get_rid_from_kid(ko_id)
    with open(ko_id + ".csv", 'a')as fout:
        header = "KOID,RID,RID-Equation,RID-Definition,CID\n"
        fout.write(header)

        if koid_namedtuple:
            for rid in koid_namedtuple.rid_list:
                res_cid = get_cid_from_rid(ko_id, rid)
                cid_list = ":".join(res_cid.cid_list)
                outline = "{},{},{},{},{}\n".format(res_cid.kid, res_cid.rid, res_cid.rid_eq, res_cid.rid_def,
                                                       cid_list)
                fout.write(outline)


if __name__ == '__main__':
    ko_id = "K00163"
    main(ko_id)
