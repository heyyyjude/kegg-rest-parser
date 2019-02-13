import os


def check_db(otu_id, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    kegg_db = 'kegg-db/ko_13_5_precalculated.tab'

    header = ''
    otu_line = ''
    with open(kegg_db)as fin:
        header = fin.readline().strip()

        for line in fin:
            tmp = line.split()
            if len(tmp) != 0:
                if tmp[0] == str(otu_id):
                    otu_line = line.strip()

    with open(output_dir + '/' + str(otu_id) + ".out.csv", 'w')as fout:
        fout.write(header + "\n")
        fout.write(otu_line + "\n")


def main(otu_id, output_dir):
    check_db(otu_id, output_dir)


if __name__ == '__main__':
    otu_id = 4347159
    output_dir = r'4347159'
    main(otu_id, output_dir)
