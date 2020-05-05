# SQL side work

from sqlConnector import getConnection
from tqdm import tqdm

# executes queries generated for insertion
def executeQueries(queries = []):
    myDBconnection = getConnection()
    mycursor = myDBconnection.cursor()
    for q in tqdm(queries):
        mycursor.execute(q)
        # print(mycursor.rowcount, "records effected.")
    mycursor.close
    myDBconnection.commit()
    myDBconnection.close

# creates insertion queries
def createQueries(table_name, year, particular, val):
    SQLcolumns = ['sNo', 'year', 'particular', 'value']
    query = "INSERT INTO %s (%s, %s, %s) VALUES ('%s', '%s', '%s')" %(table_name, SQLcolumns[1], SQLcolumns[2], SQLcolumns[3], year, particular, val)
    return (query)

# converts data frame into sql table
def df2sql(df,table_name=""):
    try:
        if table_name == "":
            from params import table_name
        df.reset_index(drop=False, inplace=True)
        years = list(df.columns)[1:]
        emptyQuery = ("TRUNCATE %s" %table_name)
        queries = [emptyQuery]
        for yr in years:
            df['queries'] = df.apply(lambda x: createQueries(table_name, yr, x['index'], x[yr]), axis=1)
            queries += list(df['queries'])
        # print(queries)
        executeQueries(queries = queries)
        return("%s updated" %table_name)
    except Exception as exp:
        return exp

# return the result of the query generated bu the user through the app
def sqlQuery(yr="",qr=""):
    myDBconnection = getConnection()
    mycursor = myDBconnection.cursor()
    from params import table_name
    q = "SELECT * from "+table_name+" WHERE year LIKE '%"+yr+"%' AND particular LIKE '%"+qr+"%'"
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    ret = []
    for i in myresult:

        data = {
        'year' : i[1],
        'particular' : i[2],
        'value' : i[3],
        }
        ret.append(data)
    print(ret)
    mycursor.close
    myDBconnection.close
    return ret,len(ret)
