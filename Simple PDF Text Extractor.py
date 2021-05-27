import glob, os
import PyPDF4


mainPath = os.getcwd()
outputPath = mainPath + '/Output'

os.chdir(mainPath + '/Input')

for infile in glob.glob('*.pdf'):	
	pdfFile = open(infile, 'rb')
	reader = PyPDF4.PdfFileReader(pdfFile)

	fullText = []
	for pageNum in range(reader.numPages):
		page = reader.getPage(pageNum)
		fullText.append(page.extractText())

	pdfFile.close()

	outfileName = "{}/{}txt".format(outputPath, infile[:-3])
	with open(outfileName, 'w') as outfile:
		for line in fullText:
			outfile.write(line)

	print('Extraction for {} completed.'.format(infile))
print('All files successfully extracted.')
