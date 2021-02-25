import glob
import os

from convert_organ_abbr_to_full_name import run_conver_rgan_abbr_to_full_name
from kegg_parser import get_cid_from_rid
from kegg_parser import get_organism_from_kid
from kegg_parser import get_rid_from_kid
from merge_picrust_output import merge_picrust_output, find_overlaps, compare_otutable_picrust


def parse_picrust_output(tsv):
    result = list()
    with open(tsv)as fin:
        fin.readline()
        for line in fin:
            ko_id = line.split(":")[0]
            result.append(ko_id)
    return result


def fetch_item_from_kegg(ko_id, path):
    if not os.path.isdir(path):
        os.makedirs(path)
    organ_entry_dict = get_organism_from_kid(ko_id)
    koid_namedtuple = get_rid_from_kid(ko_id, organ_entry_dict)

    if koid_namedtuple:
        with open(os.path.join(path, ko_id + ".csv"), 'w')as fout:
            header = "KOID,RID,RID-Equation,RID-Definition,CID,Organism\n"
            fout.write(header)

            for rid in koid_namedtuple.rid_list:
                res_cid = get_cid_from_rid(ko_id, rid)
                cid_list = ":".join(res_cid.cid_list)
                outline = "{},{},{},{},{},{}\n".format(res_cid.kid, res_cid.rid, res_cid.rid_eq, res_cid.rid_def,
                                                       cid_list, ":".join(koid_namedtuple.organism_dict.keys()))
                fout.write(outline)


def test(ko_id):
    fetch_item_from_kegg(ko_id, ko_id)


if __name__ == '__main__':
    ko_id = ['K00161', 'K00162', 'K00163', 'K00627', 'K00382']

    for i in ko_id:
        test(i)
    # output_dir_path = 'nafld-pval-0.01'
    # picrust_output = r'C:\Users\DGL8\Desktop\nafld\nalfd-picrust.pval-0.01.tsv'
    # gtest = 'C:/Users/DGL8/Desktop/nafld/gtest_fdr_0.05.csv'
    # picrust_path = output_dir_path + "/" + 'merge.output.csv'
    #
    # ko_id_list = parse_picrust_output(picrust_output)
    # for ko_id in ko_id_list:
    #     fetch_item_from_kegg(ko_id, output_dir_path)
    # csv_list = [i for i in glob.glob(os.path.join(output_dir_path, "*.csv"))]
    # for csv in csv_list:
    #     run_conver_rgan_abbr_to_full_name(csv)
    # merge_picrust_output(output_dir_path)
    # genus, species, picrust_dict = find_overlaps(gtest, picrust_path)
    # genus_dict, species_dict = compare_otutable_picrust(genus, species, picrust_dict)
    # print(genus_dict)
    # print(species_dict)
    # if you want to get organism info
    # http://rest.kegg.jp/get/gn:T04853