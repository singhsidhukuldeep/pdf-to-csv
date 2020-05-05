# handle pdf uploaded

import tabula
import pandas as pd

# converts pdf to dataframe
def pdf2df(pdfFileName=""):
    df = tabula.read_pdf(pdfFileName, pages='1')
    df = pd.DataFrame(df)
    nc = df[0][0].columns
    df[0][0].columns = list(range(len(nc)))
    df[0][0][0]
    heads = []
    years = []
    for i in range(len(nc)):
        heads.append(df[0][0][i][0])
        if df[0][0][i][0].isnumeric():
            years.append(df[0][0][i][0])
    # print(heads,years)
    allData = {}
    for i,h in enumerate(heads[:3]):
        if not h.isnumeric():
            partis = df[0][0][i][1].split("\r")
            for i in partis:
                if i =="" or "total" in i.lower():
                    partis.remove(i)
        else:
            val1 = df[0][0][i][1].split("\r")
            val2 =df[0][0][i][3].split("\r")
            # print(len(partis), len(val1), len(val2))
            data = {}
            vals = val1+val2
            for i in partis:
                data[i] = vals.pop(0)
            # print(data,allData)
            allData[h]=data
    # print(allData)
    for ii,h in enumerate(heads[3:]):
        i=ii+3
        if not h.isnumeric():
            partis = df[0][0][i][1].split("\r")
            for i in partis:
                if i =="" or "total" in i.lower():
                    partis.remove(i)
        else:
            val1 = df[0][0][i][1].split("\r")
            val2 =df[0][0][i-1][3].split("\r")
            # print(len(partis), len(val1), len(val2))
            data = {}
            vals = val1+val2
            for i in partis:
                data[i] = vals.pop(0)
            # print(data,allData)
            allData[h].update(data)
    # print(allData)
    # alldf = pd.DataFrame(allData).reset_index(drop=False, inplace=False)
    alldf = pd.DataFrame(allData)
    # print(alldf.head(25))
    return alldf

# converts pdf to csv
def pdf2csv(pdfFileName="", csvFileName=""):
    df = pdf2df(pdfFileName)
    df.to_csv(csvFileName)
    return csvFileName
