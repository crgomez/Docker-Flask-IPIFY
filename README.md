# Docker-Flask-IPIFY
Flask app to get your public IP address programmatically.

# API Usage
Using ipify is very simple.

## IPv4 API
```
API URL	Response         Type	  Sample Output (IPv4)
https://api.ipify.org	 text	    98.207.254.136
```

## IPv6 API
```
API URL	Response         Type	  Sample Output (IPv6)
https://api6.ipify.org	 text	  2a00:1450:400f:80d::200e
```

## Docker Build
```
docker build -t flask-ipify:v1.0.0 .
```

## Docker Run
```
docker run -dit --name getip -p 5000:5000 flask-ipify:v1.0.0
```

## Docker Output

Open your browser to http://localhost:5000

or

```
curl http://localhost:5000
```
