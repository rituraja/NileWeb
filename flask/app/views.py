from app import app
from flask import render_template, jsonify
import happybase

project = {'name':'Nile',
    'desc': 'Sales Analytics' 
}

@app.route('/')
@app.route('/index')
def batch():
    return render_template('batch.html',
        title='Insight Data Engineering Project',
        project = project)

@app.route('/realtime')
def realtime():
    return render_template('realtime.html',
        title='Insight Data Engineering Project',
        project = project)

@app.route("/hbase/")
def hbase_test():
    connection = happybase.Connection('54.183.25.144')
    my_table = connection.table('productCounts')
    key6 = my_table.row('Romance')
    return key6['f:c1']

@app.route('/showChart1')
def showChart1():
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('productCounts')
    data = hbase_table.scan()
    datalist = []
    for key, value in data:
        datalist.append([key,int(value['f:c1'])])
    
    dataChart1 = {
        'series' : [{"type": 'pie',"name": 'categories', "data": datalist}],
        'title' : {"text": 'Product Distribution by Category'},
    }
    return jsonify(dataChart1)

@app.route('/_showTable')
def showTable():
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('productCounts')
    data = hbase_table.scan()

    return render_template('cate_prod.html' , data = data )

@app.route("/api/getProductsPerCategory")
def api_ProCat():
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('productCounts')
    data = hbase_table.scan()

    return dump(data)

@app.route("/api/getSalesPerCategory_daily/<day>")
def api_scd(day = '2014-12-28'):
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('salesCatPerDay')
    data = hbase_table.scan(row_prefix=day)
    datalist = []
    xAxislist = []
    for key, value in data:
        datalist.append(int(value['f:c1']))
        xAxislist.append(key[11:])
    
    dataChart = {
        'series' : [{"name": day , "data": datalist}],
        'title' : {"text": 'Day Sales'},
        'xAxis' : {"categories": xAxislist},
        'yAxis' : {"min" : 1000, "title": {"text": 'Product Count'}},
    }

    return jsonify(dataChart)

@app.route("/api/getSalesPerCategory_monthly/<month>")
def api_scm(month = '2014_12'):
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('salesCatPerMth')
    data = hbase_table.scan(row_prefix=month)
    datalist = []
    xAxislist = []
    for key, value in data:
        datalist.append(int(value['f:c1']))
        xAxislist.append(key[8:])
    
    dataChart = {
        'series' : [{"name": month , "data": datalist}],
        'title' : {"text": 'Monthly Sales'},
        'xAxis' : {"categories": xAxislist},
        'yAxis' : {"min" : 30000 , "title": {"text": 'Product Count'}},
    }

    return jsonify(dataChart)

@app.route("/api/getProductsPerRegion_monthly/<value>")
def api_prm(value = None):
    connection = happybase.Connection('54.183.25.144')
    hbase_table = connection.table('salesPerZipcode')
    data = hbase_table.scan()
    return dump(data)

def dump1(recordset):
    str = ''
    for key , data in recordset:
        str = str +  key + ' - ' + data['f:c1'] + '<BR>'
    return str
