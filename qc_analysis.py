from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

for record in SeqIO.parse("D:\Project Biopyhton By Muhammad Ali\data\input_sequence.fasta", "fasta"):
    sequence_length = len(record.seq)
    gc_content = gc_fraction(record.seq) * 100

print("Sequence ID:", record.id)
print("Sequence Length:", sequence_length)
print("GC Content (%):", gc_content)

if sequence_length >= 300 and 30 <= gc_content <= 70:
    print("Sequence Passed Quality Filtering")
    SeqIO.write(record, "D:\Project Biopyhton By Muhammad Ali\data\input_sequence.fasta", "fasta")
else:
    print("Sequence Failed Quality Filtering")

from Bio.Blast import NCBIWWW
result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",  # protein collection database
    sequence="MAQIDFRKKINWHRRYRSPQGVKTEHEILRIFESDRGRIINSPAIRRLQQKTQVFPLERNAAVRTRLTHSMEVQQVGRYIAKEILSRLKELKLLEAYGLDELTGPFESIVEMSCLMHDIGNPPFGHFGEAAINDWFRQRLHPEDAESQPLTDDRCSVAALRLRDGEEPLNELRRKIRQDLCHFEGNAQGIRLVHTLMRMNLTWAQVGGILKYTRPAWWRGETPETHHYLMKKPGYYLSEEAYIARLRKELNLALYSRFPLTWIMEAADDISYCVADLEDAVEKRIFTVEQLYHHLHEAWGQHEKGSLFSLVVENAWEKSRSNSLSRSTEDQFFMYLRVNTLNKLVPYAAQRFIDNLPAIFAGTFNHALLEDASECSDLLKLYKNVAVKHVFSHPDVERLELQGYRVISGLLEIYRPLLSLSLSDFTELVEKERVKRFPIESRLFHKLSTRHRLAYVEAVSKLPSDSPEFPLWEYYYRCRLLQDYISGMTDLYAWDEYRRLMAVEQ"
    )
with open("blastp_result.xml", "w") as b:  
    b.write(result_handle.read())  
print("BLAST search completed successfully")  

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
           