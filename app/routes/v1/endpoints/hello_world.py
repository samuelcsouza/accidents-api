from socketify_app import app

router = app.router()

@router.get("/hello")
def hello_world(res, req):
    res.end({"hello": "world!"})

@router.get("/")
def home(res, req):
    res.end({"Socketify": "Python!"})
