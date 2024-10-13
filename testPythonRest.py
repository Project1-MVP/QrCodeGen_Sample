#https://reintech.io/blog/create-web-service-python
'''
pip install Flask
pip install requests
https://www.geeksforgeeks.org/get-post-requests-using-python/
'''
import time
import requests
 
# api-endpoint
Node1URL = "http://localhost:3001/tasks"
Node2URL = "http://localhost:3002/tasks"
LBURL = "http://localhost:9090/tasks"
Node1GetURL = "http://localhost:3001/tasks/1b7d6c02342c44a39a28946e41211cb6"
Node2GetURL = "http://localhost:3002/tasks/1b7d6c02342c44a39a28946e41211cb6"
data = {'title': 'Learn Python Microservices',
        'description': 'Learn how to create a web service with Python',
        'completed': True}
def measureThroughPut(nodeName,URL,duration):
    count=0
    b=time.time()
    while True:
        r=requests.post(url=URL, json=data)
        #r=requests.get(url=URL)
        e=time.time()
        diff = e-b
        count+=1
        if (diff>duration):
            break
    #end While True
    print(f"{nodeName}:{count}/{duration} (hits/secs)")
bt=time.time()
if False: #Threading
    import threading

    thr1 = threading.Thread(target=measureThroughPut, args=("Node1",Node1URL,10), kwargs={})
    thr2 = threading.Thread(target=measureThroughPut, args=("Node2",Node2URL,10), kwargs={})
    thr1.start() # Will run "foo"
    thr2.start() # Will run "foo"
    #thr.is_alive() # Will return whether foo is running currently
    thr1.join() # Will wait till "function" is done
    thr2.join() # Will wait till "function" is done

if True: #Sequential
    measureThroughPut("Node1",Node1URL,10)
    measureThroughPut("Node2",Node2URL,10)


et=time.time()
print(f"Duration:{et-bt}")    
'''
print(time.time())
for i in range (100):
    r = requests.get(url = Node2URL)
print(time.time())
#data = r.json()
data = {'title': 'Learn Python Microservices',
        'description': 'Learn how to create a web service with Python',
        'completed': True}
 
print(time.time())
for i in range (100):
    r = requests.post(url=URL, json=data)
print(time.time())
print (r.text)
'''
# extracting data in json format

#print (data)
'''
# extracting latitude, longitude and formatted address
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
 
# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
    %(latitude, longitude,formatted_address))
    '''