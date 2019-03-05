# Micro Service With Python and Flask. 

[Howto](https://medium.com/@ssola/building-microservices-with-python-part-i-5240a8dcc2fb)

To install Python 3.6 on cloud 9: [python-3.6.4](https://gist.github.com/barbietunnie/0f26219ab286e416ddcbf6aece4279d2)

```
sudo apt-get install libssl-dev openssl
wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz
tar xzvf Python-3.6.4.tgz
cd Python-3.6.4.tgz
./configure
make
sudo make install

# Check if python 3.6 is installed
python3.6

# If python 3.6 is not installed, run the command below
sudo ln -fs /opt/Python-3.6.4/Python /usr/bin/python36
```

### Stack:

 - Flask (Framework)
 - Flask-Injector (For injecting dependencies required in classes/methods)
 - Connexion (Mapping API requests to python functions)
 - Avro (Serialization Tool) 

API Documentation with swagger. 