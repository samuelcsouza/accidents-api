from socketify import App
from utils.errors_handler import raise_error_route_not_found, error_handler

app = App()
router = app.router(prefix="/v1")

app.set_error_handler(error_handler)
app.any("/*", raise_error_route_not_found)