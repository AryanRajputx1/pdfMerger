import PyPDF2


pdffiles = ['1.pdf', '2.pdf']


merger = PyPDF2.PdfMerger()

# Loop through each file in the pdffiles list
for filename in pdffiles:

    pdfReader = PyPDF2.PdfReader(filename)


    merger.append(pdfReader)

# Write the merged PDF to an output file
merger.write('merged.pdf')


merger.close()



