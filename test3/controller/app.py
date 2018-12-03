from flask import Flask,jsonify,request,render_template
from flask_cors import CORS


app = Flask(__name__, static_url_path='/assets')
CORS(app)

listBerat = [
    {'tanggal':'2018-08-22', 'max':50, 'min':49},
    {'tanggal':'2018-08-21', 'max':49, 'min':49},
    {'tanggal':'2018-08-20', 'max':52, 'min':50},
    {'tanggal':'2018-08-19', 'max':51, 'min':50},
    {'tanggal':'2018-08-18', 'max':50, 'min':48}
]

# @app.route('/')
# def home():
#   return render_template('index.html')

# @app.route('/update')
# def update():
#   return render_template('update.html')

# @app.route('/detail')
# def detail():
#   return render_template('detail.html')

#get /store
@app.route('/berat')
def get_list():
  if len(listBerat) == 0 :
    return jsonify({'tanggal':'0000-00-00', 'max':0, 'min':0})
  return jsonify(listBerat)

#mengambil list data
@app.route('/berat/<string:tanggal>')
def get_berat(tanggal):
  for berat in listBerat:
    if berat['tanggal'] == tanggal:
          return jsonify(berat)
  return jsonify ({'message': 'data not found'})

#tambah/edit data
@app.route('/berat' , methods=['POST'])
def tambah_data():
  request_data = request.get_json()
  new_data = {
    'tanggal':request_data['tanggal'],
    'max':int(request_data['max']),
    'min':int(request_data['min'])
  }
  for berat in listBerat:
    if berat['tanggal'] == new_data['tanggal']:
        berat.update(new_data)
        return jsonify(new_data)
  listBerat.append(new_data)
  return jsonify(new_data)

#menghapus data
@app.route('/hapus', methods=['POST'])
def delete_data():
  request_data = request.get_json()
  tanggal = request_data['tanggal']
  global listBerat
  listBerat = list(filter(lambda x: x['tanggal'] != tanggal, listBerat))
  return 'item deleted'

@app.route('/ratarata')
def ratarata():
  if len(listBerat) == 0:
    return jsonify({'max':0, 'min':0})
  max = [l['max'] for l in listBerat]
  min = [l['min'] for l in listBerat]

  return jsonify({'max': sum(max)/len(max), 'min': sum(min)/len(min)})


app.run(host='0.0.0.0', port=5544)
