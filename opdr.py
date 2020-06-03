from flask import Flask, render_template, request
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

import vier
from vier import *

app = Flask(__name__)

# werd iedere keer in langzame rij gezet, dus wanneer je hem runt krijg je resultaten van hieronder.
# natuurlijk kan je ook gewoon zoeken in de webpagina zelf en krijg je ook je resultaten :)

@app.route('/')
def afv():
    seq = request.args.get('seq', '')
    if seq == '':
        seq = 'GTCGTGGTCCGAGGTCTCCGACAAGCCCTCGGCATTCCCGCCGGACGCACACACGCACGACTGGGGT' \
              'GACCTCACCGGCCTGCCTGACTACGCTACTCGTTGGCCGTCGTGGTCCGAGGTCTCCGACAAGCCCT' \
              'GGCATTCCCGCCGAGTGCGCATACGCATTCGGCGGACGACGTCACGTCCGGGACACTCCCGGTC' \
              'TCCCGCGGTGGCACAGGGCGGACGTCGCTCACGAGCGGAGCGTTGCTCGTCGGCGCCGGTAGTTC' \
              'GGCGATCGCAGGTGTAAGCGTAGGGACGGCAGGTCAA'
    else:
        pass
    b = vier.blast(seq)
    messenger_rna = transcriptie(seq)
    ei = translatie(messenger_rna)
    return render_template("afv4.html", seq=seq, b=b,
                           messenger_rna=messenger_rna, ei=ei)


def transcriptie(seq):
    dna = Seq(seq, IUPAC.unambiguous_dna)
    messenger_rna = dna.transcribe()
    print('rna', messenger_rna)

    return messenger_rna


def translatie(messenger_rna):
    ei = messenger_rna.translate()
    print('ei', ei)
    return ei


if __name__ == '__main__':
    app.run()
