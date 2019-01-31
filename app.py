from flask import Flask, jsonify 

app = Flask(__name__)

parcels = [
    {
        'serial': 1,
        'item': 'necklace',
        'Recievers Email Address': 'favourgrl254@gmail.com',
        'Pick-up Location': 'Nairobi',
        'Delivery destination': 'Kilifi'
    },
    {
        'serial': 2,
        'Item': 'curl sponge',
        'Recievers Email Address': 'victorianzale234@gmail.com',
        'Pick-up Location': 'Nairobi',
        'Delivery destination': 'Kilifi'
    }
]

@app.route('/api/v2/parcels', methods=['GET'])
def get_parcels():
    return jsonify({'parcels': parcels})

if __name__ == '__main__':
    app.run(debug=True) 