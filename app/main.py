from socketify_app import app

import routes.v1.endpoints.hello_world

def home(res, req):
    res.end({"pypy3": "Hello World socketify from Python!"})

app.get("/", home)


app.listen(3000, lambda config: print("Listening on port http://localhost:%d now\n" % config.port))

app.run()