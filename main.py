from flask import Flask, jsonify, request, render_template

app = Flask('app')

stores = []


@app.route('/')  # 'home page'
def home():
  return render_template('index.html')
  
@app.route('/store', methods=['POST'])  # 'create store'
def create_store():
    request_data = request.get_json()
    stores.extend([{'name': request_data['name'], 'items': []}])
    return jsonify({'stores': stores})

@app.route('/store')  # 'create store'
def get_store():
    return jsonify({'stores': stores})
  
@app.route('/store/<string:name>/item', methods=['POST'])  # 'create store'
def create_item(name):
    request_data = request.get_json()
    for store in stores:
      if store['name']==name:
        new_item={
          'name' :request_data['name'],
          'price' :request_data['price']
        }
        store['items'].append(new_item)
        return jsonify({'items':  store['items']})
    return "store not found"
  
@app.route('/store/<string:name>/item')  # 'create store'
def getting_item(name):
    request_data = request.get_json()
    for store in stores:
      if store['name']==name:
        return jsonify({'items':  store['items']})
    return "store not found"
app.run(host='0.0.0.0', port=8080)
