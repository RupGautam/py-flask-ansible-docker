## Dockerizing Flask application with CI/CD
### Prerequsite for local 
- Docker
- Docker-compsoe
- Ansible
- Flask
- Virtualenv


### Build Application Locally
```
$ git clone https://github.com/RupGautam/py-flask-ansible-docker.git
$ cd py-flask-ansible-docker
# Create python venv
$ python3 -m venv env
# Activate venv
$ source env/bin/activate
```
#### Installing pip requirements
```
$ pip install pip --upgrade
$ pip install -r app/requirements.txt
```  

#### Running the application locally
```
$ gunicorn -w 2 -b :8000 app:app
```
You should be able to access webpage [localhost:8000](http://localhost:8000)


### Build Application for Docker
```
# Make sure you have installed docker and docker-compose 
$ docker-compose up -d --build
or
$ docker build <image-name>:<v1> .
$ docker run -d -p 80:80 -p 8000:8000 <image-name>:<v1>
```

### Deploying Application with Ansible
```
# Make sure you have install anisble and ansible-playbook
$ vi ansible/hosts
# Make necessary change for your inventories 
$ cd ansible
$ ansible-playbook site.yml
```
Once `ansible-playbook` is finished; you should be able to acess your application <ip-address>


