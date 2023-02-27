from socketify_app import app
import routes
from database import get_mongo, close_connection

app.listen(3000, lambda config: print("Listening on port http://localhost:%d now\n" % config.port))

@app.on_start
def on_start():
    get_mongo()


@app.on_shutdown
def on_stop():
    close_connection()


app.run()
