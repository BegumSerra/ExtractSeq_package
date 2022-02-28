from Bio import SeqIO

def seqs_annot(proteome, annot):
    outgroups=[]
    sseqid = ['tr|Q1DDB1|Q1DDB1_MYXXD', 'tr|Q9HYZ4|Q9HYZ4_PSEAE', 'sp|O31613|YJBO_BACSU', 'tr|Q39Q27|Q39Q27_GEOMG']
    for record in SeqIO.parse(proteome, "fasta"):
        if (record.id).rstrip() in sseqid:
            outgroups.append(record)
    SeqIO.write(outgroups, annot, "fasta")
    return annot

