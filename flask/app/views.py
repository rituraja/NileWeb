from app import app
from flask import render_template
import happybase

@app.route('/')
@app.route('/index')
def index():
    project = {'name':'Nile',
                'desc': 'Sales Analytics' 
    }
    return render_template('index.html',
        title='Nile Sales Analytics',
        project = project)

@app.route("/hbase/")
def hbase_test():
    connection = happybase.Connection('54.183.25.144')
    my_table = connection.table('productCounts')
    key6 = my_table.row('Romance')
    return key6['f:c1']

@app.route('/presentation')
def presentation():
    return render_template('presentation.html')

@app.route('/history_blocks')
def history_blocks():
    return render_template('history_blocks.html')

@app.route('/history_transactions')
def history_transactions():
    return render_template('history_transactions.html')

@app.route('/history_prices')
def history_prices():
    return render_template('history_prices.html')


@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/api')
def api_index():
    return render_template('api.html')

@app.route('/wallets')
def wallets():
    return render_template('wallets.html')

@app.route('/wallets_timed')
def wallets_timed():
    return render_template('wallets_timed.html')


@app.route("/api/getProductsPerCategory")
def api_ProCat():
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('productCounts')
    data = hbase_table.scan()

    return dump(data)

@app.route("/api/getSalesPerCategory_daily/<value>")
def api_scd(value = None):
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('salesCatPerDay')
    data = hbase_table.scan()
    return dump(data)

@app.route("/api/getSalesPerCategory_monthly/<value>")
def api_scm(value = None):
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('salesCatPerMth')
    data = hbase_table.scan()
    return dump(data)

@app.route("/api/getProductsPerRegion_monthly/<value>")
def api_prm(value = None):
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('salesPerZipcode')
    data = hbase_table.scan()
    return dump(data)

def dump(recordset):
    str = ''
    for key , data in recordset:
        str = str +  key + ' - ' + data['f:c1'] + '<BR>'
    return str

