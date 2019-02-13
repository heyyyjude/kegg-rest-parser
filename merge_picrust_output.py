import glob
from collections import defaultdict


def merge_picrust_output(path):
    # results = set()
    results = defaultdict(set)
    output_list = [i for i in glob.glob(path + "/*output*")]
    for i in output_list:
        with open(i)as fin:
            fin.readline()
            for line in fin:
                line = line.strip()
                tmp = line.split(",")
                organism = tmp[-1].split("|")
                ko_id = tmp[0]

                if len(organism) != 1:
                    for organ in organism:
                        results[ko_id].add(organ)

    with open(path + "/merge.output.csv", 'w')as fout:
        for ko_id in results:
            for speices in results[ko_id]:
                fout.write(ko_id + "," + speices + "\n")


def find_overlaps(gtest, picrust):
    genus = set()
    species = set()
    # key = ko-id, value = set(speices, speices...)
    picrust_dict = defaultdict(set)

    with open(gtest)as fin:
        for line in fin:
            line = line.strip()
            tmp = line.split()
            gen = tmp[0]
            spec = line
            genus.add(gen)
            species.add(spec)
    with open(picrust)as fin:
        for line in fin:
            line = line.strip()
            tmp = line.split(",")
            ko_id = tmp[0]
            organ = tmp[1]
            picrust_dict[ko_id].add(organ)

    return genus, species, picrust_dict


def compare_otutable_picrust(genus, species, picrust_dict):
    genus_dict = defaultdict(set)
    speices_dict = defaultdict(set)
    for i in genus:
        for ko_id in picrust_dict:
            for j in picrust_dict[ko_id]:
                if i in j:
                    genus_dict[ko_id].add(i)

    for i in species:
        for ko_id in picrust_dict:
            for j in picrust_dict[ko_id]:
                if i in j:
                    speices_dict[ko_id].add(j)
    return genus_dict, speices_dict


def write_results(path, species_dict):
    with open(path + "/final.speices.csv", 'w')as fout:
        for ko_id in species_dict:
            for species in species_dict[ko_id]:
                fout.write(ko_id + "," + species + "\n")

    # key ko-id value set(species, species, species)


def get_overlap_count(genus_dict):
    result = set()
    for koid in genus_dict:
        for genus in genus_dict[koid]:
            result.add(genus)
    print(result)
    print(len(result))


if __name__ == '__main__':
    path = r'nafld-pval-0.01'
    merge_picrust_output(path)
    gtest = 'C:/Users/DGL8/Desktop/nafld/gtest_fdr_0.05.csv'
    picrust = path + "/" + 'merge.output.csv'
    genus, species, picrust_dict = find_overlaps(gtest, picrust)
    genus_dict, species_dict = compare_otutable_picrust(genus, species, picrust_dict)
    # print(species_dict)
    write_results(path, species_dict)
    get_overlap_count(genus_dict)
    print(genus_dict)
    print(species_dict)