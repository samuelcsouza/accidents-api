from socketify_app import app
import routes


app.listen(3000, lambda config: print("Listening on port http://localhost:%d now\n" % config.port))

app.run()