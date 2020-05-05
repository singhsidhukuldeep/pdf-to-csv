# testing to check functionality of indvidual functions

from readPDF import pdf2df, pdf2csv

print(pdf2df(pdfFileName = "../data/BalSheet.pdf"), end="\n\n")
print(pdf2csv(pdfFileName = "../data/BalSheet.pdf", csvFileName="../data/testOut.csv"), end="\n\n")


from sqlConnector import getConnection

print(getConnection(), end="\n\n")


from dbQuery import df2sql

print(df2sql(df=pdf2df(pdfFileName = "../data/BalSheet.pdf")))

from dbQuery import sqlQuery
sqlQuery(yr = "2015",qr="discount")
