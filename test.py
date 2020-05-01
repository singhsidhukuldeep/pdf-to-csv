from readPDF import pdf2df, pdf2csv

print(pdf2df(pdfFileName = "./data/BalSheet.pdf"))
print(pdf2csv(pdfFileName = "./data/BalSheet.pdf", csvFileName="./data/testOut.csv"))
