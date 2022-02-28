import pandas as pd

def read(blast):
	df= pd.read_csv(blast, sep='\t', names = ["qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "sseq"])
	sseqid = df["sseqid"].values.tolist()
	print(sseqid)
	return(sseqid)

