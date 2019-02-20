import os,sys
from pikepdf import Pdf

def unlockPdf(filepath):
		PSWD = os.path.basename(filepath)[0:-4]
		pdffile = Pdf.open(filepath,password=PSWD)
		newPdf = Pdf.new()
		newPdf.pages.extend(pdffile.pages)
		OUTPUT_DIR = os.path.dirname(filepath)
		newPdf.save(OUTPUT_DIR + '/decrypted.pdf')

FILE_PATH = sys.argv[1]
unlockPdf(FILE_PATH)
