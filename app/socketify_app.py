from socketify import App
from utils.errors_handler import raise_error_route_not_found, error_handler
from app.dependencies import decode_token


app = App()


router = app.router("/v1", decode_token)

app.set_error_handler(error_handler)
app.any("/*", raise_error_route_not_found)
