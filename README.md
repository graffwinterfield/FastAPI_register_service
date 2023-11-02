# FastAPI_register_service

# install docker and python
<pre>
sudo apt update
sudo apt install docker-compose python3
</pre>

# download project
<pre>
git clone https://github.com/graffwinterfield/FastAPI_register_service.git
cd FastAPI_register_service/
pip install -r requirments.txt
docker-compose up -d
</pre>
# start
<pre>
python3 main.py
</pre>
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/878aa8af-a6fd-46b9-ab86-1aa7cafdb92d)


# usage
<pre>
http://127.0.0.1:8000/docs#/
в моем случае адрес: 192.168.31.79 так как я запускал на виртуалке
</pre>
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/96ec8e16-26b4-450c-b988-6e55a2db6819)


# create request
<pre>
curl -X 'POST' \
  'http://192.168.31.79:8000/api/note/create?user_id=7765fcfaa0f14asdfaf&target_id=2&key=registration' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{}'
</pre>
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/84eb429e-96ba-4217-aaaa-a5731a8a42bd)
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/2a7ec7f4-52f8-43a9-8302-90e469769502)

# list request
<pre>
curl -X 'GET' \
  'http://192.168.31.79:8000/api/note/list?user_id=7765fcfaa0f14asdfaf&skip=0&limit=10' \
  -H 'accept: application/json'
</pre>
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/93cfa14c-899b-4ff6-8b0d-4ff7cc11c50b)

# read request
<pre>
curl -X 'POST' \
  'http://192.168.31.79:8000/api/note/read?user_id=7765fcfaa0f14asdfaf&notification_id=1' \
  -H 'accept: application/json' \
  -d ''
</pre>
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/7122144a-0e70-44ff-88e8-4cd95a57fd92)
![image](https://github.com/graffwinterfield/FastAPI_register_service/assets/110451740/5ccd04dc-6dfc-4002-bd3b-03ee13a48f5e)

