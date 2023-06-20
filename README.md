An application created for kubernetes liveness or readiness probe

If you request **/healthz** endpoint, this app will return you 200 http status code. However, if you want to change the http status code, you can request the **/change** endpoint.

For example:

```
curl -LI localhost:5000/healthz
```
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.8.9
Date: Wed, 11 Jan 2023 19:01:54 GMT
Content-Type: application/json
Content-Length: 17
Connection: close
```
We changing now http status code:

```
curl -LI http://localhost:5000/change\?status_code\=500
```

and then reqeust to **/healthz** endpoint

```
curl -LI localhost:5000/healthz
```
```
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: Werkzeug/2.2.2 Python/3.8.9
Date: Wed, 11 Jan 2023 19:03:23 GMT
Content-Type: application/json
Content-Length: 17
Connection: close
```

If you need sample application for liveness and readiness probe testing. You can use this application.
