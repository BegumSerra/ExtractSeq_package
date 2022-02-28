from Bio import SeqIO

def seqs_ids(annot, ids):
    with open(annot) as handle:
        accession=[]
        for record in SeqIO.parse(handle, "fasta"):
            record.id=record.id.split("|")[1]
            record.description=""
            accession.append(record)
        SeqIO.write(accession, ids, "fasta")
        return ids
