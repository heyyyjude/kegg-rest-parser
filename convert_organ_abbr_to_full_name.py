import glob
import os


def parse_organism_db():
    organism_db = r'E:\work\Microbiome\PICRUSt\org.db.tsv'
    result = dict()
    with open(organism_db)as fin:
        fin.readline()
        for line in fin:
            tmp = line.split('\t')
            organism = tmp[1]
            species = tmp[2]
            result[organism] = species
    return result


def write_results(organ_dict, csv_input):
    with open(csv_input)as fin, open(csv_input + ".output.csv", 'w')as fout:
        fout.write(fin.readline())
        for line in fin:
            species_list = list()
            pre_line = line.rsplit(",", 1)[0]
            post = line.rsplit(",", 1)[-1]
            abbr_list = post.split(":")
            for abbr in abbr_list:
                if abbr in organ_dict:                    species_list.append(organ_dict[abbr])
            post_outline = "|".join(species_list)
            outline = pre_line + "," + post_outline
            fout.write(outline + '\n')


def run_conver_rgan_abbr_to_full_name(csv_input):
    organ_db = parse_organism_db()
    write_results(organ_db, csv_input)


if __name__ == '__main__':
    pass
    #csv_path = 'nafld-pval-0.005'
    #csv_list = [ i for i in glob.glob(os.path.join(csv_path, "*.csv"))]
    #for csv in csv_list:
    #    run_conver_rgan_abbr_to_full_name(csv)
