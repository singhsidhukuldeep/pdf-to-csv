# flask app

from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
import params
from readPDF import pdf2df, pdf2csv
from dbQuery import df2sql, sqlQuery
app = Flask(__name__)

# route to show the main page
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        qr = request.form['qr']
        yr = request.form['yr']
        # inputfile = request.form['inputfile']
        f = request.files['inputfile']
        f.save(secure_filename(params.local_pdf))
        print(request.form)
        try:
            df = pdf2df(pdfFileName = params.local_pdf)
            pdf2csv(pdfFileName = params.local_pdf, csvFileName= params.local_csv)
            df2sql(df=df)
            res = sqlQuery (qr = qr, yr = yr)
            return render_template ('index.html', res = res[0], found = res[1])
        except Exception as exp:
            return "ERROR: "+str(request.form) + str(exp)
        pass
    else:
        res = []
        found = -1
        return render_template ('index.html', res = res, found = found)

# route download the csv on button click
@app.route('/download')
def download_file():
    return send_file(params.local_csv, as_attachment=True)

if __name__ == "__main__":
    app.run(debug =True)
