from flask import Flask,jsonify,request

app = Flask(__name__)
contacts = [
    {
        'id' : 1,
        'contact' : 9672831131,
        'name' : 'Tony Stark',
        'done' : False
    },
    {
        'id' : 2,
        'contact' : 9899320131,
        'name' : 'Bruce Banner',
        'done' : False
    }
]
@app.route('/')
def hello_world():
    return 'My second API. Contact!'

@app.route('/add-data',methods = ['POST'])
def add_contact():
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message' : 'Please provide the data'
        },400)
    contact = {
        'id' : contacts[-1]['id'] + 1,
        'name' : request.json['name'],
        'conatct' : request.json.get('contact',''),
        'done' : False
    }
    contacts.append(contact)
    return jsonify({
        'status' : 'Success',
        'message' : 'Contact added successfully!'
    })

@app.route('/get-data')
def get_tasks():
    return jsonify({
        'data' : contacts
    })

if(__name__ == '__main__'):
    app.run(debug= True)