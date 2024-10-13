from datetime import datetime
import os
from uuid import uuid4
from flask import Flask, jsonify, request

#import uuid
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import ssl
ssl.DEFAULT_CIPHERS = 'DEFAULT@SECLEVEL=1'

app = Flask(__name__)

#conStr="mongodb+srv://chandrabhaskaras:mongo2024@cluster0.wakzrbn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
conStr=os.environ.get('mongo')
# Create a new client and connect to the server
client = MongoClient(conStr, server_api=ServerApi('1'), ssl=True)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("ExceptionOccurred While Connecting to Mongo DB")
    print(e)
mydb = client["Chandra"]
mycol = mydb["QRRepo"] #collection

#getVacantQRCount
#getFreshQR
#assignQR
'''
http://127.0.0.1:5000/getVacantQRCount
http://127.0.0.1:5000/getFreshQR
http://127.0.0.1:5000/
http://127.0.0.1:5000/
'''

@app.route('/')
def hello_QRProvisionerService():
    return 'QR Provisioner Service!'

@app.route('/getVacantQRCount', methods=['GET'])
def getVacantQRCount():
    #count=mycol.count_documents({ "State": "VacantQR" })
    count=mycol.count_documents({})
    #print("No of Documents:",count)
    return str(count)

@app.route('/getFreshQR', methods=['GET'])
def getFreshQR():
    count=mycol.count_documents({})
    if(count<10):
        for i in range(10):
            UniqueID = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4()) #locally generated
            body = { "_id": UniqueID, "State": "VacantQR", "Generated Time": datetime.now().strftime('%Y%m-%d%H-%M%S-') }
            x = mycol.insert_one(body)
        
    oneFreshQR=mycol.find_one_and_delete({})
    return oneFreshQR

'''
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': uuid.uuid4().hex,
        'title': request.json['title'],
        'description': request.json['description'],
        'completed': request.json.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify({'task': new_task})

@app.route('/tasks/count', methods=['GET'])
def count_task():
    return jsonify({'taskCount': tasks.count()})

@app.route('/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    return jsonify({'task': task[0]})

@app.route('/tasks/<string:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['completed'] = request.json.get('completed', task[0]['completed'])
    return jsonify({'task': task[0]})

@app.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'error': 'Task not found'})
    tasks.remove(task[0])
    return jsonify({'result': 'Task deleted'})
'''
print (__name__)
if __name__ == '__main__':
    print ("Python running on docker")
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
