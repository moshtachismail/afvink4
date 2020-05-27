from flask import Flask, render_template, request
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

app = Flask(__name__)


@app.route('/')
def afv():
    coding_dna = request.args.get('sequence', '')
    messenger_rna= transcriptie(coding_dna)
    ei = translatie(messenger_rna)
    return render_template("afv4.html", coding_dna=coding_dna, messenger_rna=messenger_rna, ei=ei)

def transcriptie(coding_dna):
    dna = Seq(coding_dna, IUPAC.unambiguous_dna)
    messenger_rna= dna.transcribe()

    return messenger_rna

def translatie(messenger_rna):
    ei = messenger_rna.translate()
    #print(translatie)

    return ei



if __name__ == '__main__':
    app.run()

