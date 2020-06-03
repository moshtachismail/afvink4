from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SearchIO


# from opdr import *

def blast(seq):
    result_handle = NCBIWWW.qblast("blastx", "nr", seq)
    print(result_handle)
    # blast_records = NCBIWWW.parse(result_handle)
    # print (blast_records)
    with open("derde.xml", 'w') as out_handle:
        out_handle.write(result_handle.read())

    with open("derde.xml", 'r') as out_handle:
        blast_records = NCBIXML.parse(out_handle)
        blast_record = next(blast_records)
        # print(blast_record)
        E_VALUE_THRESH = 0.04
        #max_hsps = 1
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print("****Alignment****")
                    title = ("sequence:", alignment.title)
                    # print("length:", alignment.length)
                    # print("e value:", hsp.expect)
                    # print(hsp.query[0:75] + "...")
                    # print(hsp.match[0:75] + "...")
                    # print(hsp.sbjct[0:75] + "...")

        blast_qresult = SearchIO.read("derde.xml", "blast-xml")
        blast_hsp = blast_qresult[0][0] # alleen informatie van eerste hit word meegenomen
        print(blast_hsp)

    return blast_hsp

# def main():
#     seq = 'GTCGTGGTCCGAGGTCTCCGACAAGCCCTCGGCATTCCCGCCGGACGCACACACGCACGACTGGGGT' \
#           'GACCTCACCGGCCTGCCTGACTACGCTACTCGTTGGCCGTCGTGGTCCGAGGTCTCCGACAAGCCCT' \
#           'GGCATTCCCGCCGAGTGCGCATACGCATTCGGCGGACGACGTCACGTCCGGGACACTCCCGGTC' \
#           'TCCCGCGGTGGCACAGGGCGGACGTCGCTCACGAGCGGAGCGTTGCTCGTCGGCGCCGGTAGTTC' \
#           'GGCGATCGCAGGTGTAAGCGTAGGGACGGCAGGTCAA'
#     blast(seq)

#     messenger_rna = transcriptie(seq)
#     ei = translatie(messenger_rna)


