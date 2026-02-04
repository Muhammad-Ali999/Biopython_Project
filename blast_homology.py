from Bio.Blast import NCBIXML
with open(r"D:\Project Biopyhton By Muhammad Ali\data\blastp_result.xml") as r:
    blast_record = NCBIXML.read(r)

print('Number of alignments:', len(blast_record.alignments))
best_alignment = blast_record.alignments[:10]    

for alignment in best_alignment:
    print('Alignment title:', alignment.title)
    print('Length:', alignment.length)
    for hsp in alignment.hsps:
        print('E-value:', hsp.expect)
        print("Score:", hsp.score)
        print("Query sequence:", hsp.query)
        print("Alignment match:", hsp.match)
        print("Matched sequence:", hsp.sbjct)
        print("Query range:", hsp.query_start, "-", hsp.query_end)
        print("Subject range:", hsp.sbjct_start, "-", hsp.sbjct_end)
    print("--"*50) 

print('Evolutionary hints found in:')

count = 1
for alignment in best_alignment:
    if any(hsp.expect < 0.01 for hsp in alignment.hsps):
        print('Alignment title',count, ':', alignment.title)
        count += 1