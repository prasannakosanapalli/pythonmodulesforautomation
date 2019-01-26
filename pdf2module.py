import pypdf2

a=pypdf2.pdffilereader(path or filename or variable)
a.numpages()
b=a.getpage(1)
c=b.extracttext()

a.isencrypted()
a.decrypt("password")

d=pypdf2.PdfFileWriter()
d.addpage(b)
a.close()
filewriter
a.mergepage(b)

pdfwriter.encrypt("password")
a.close()
