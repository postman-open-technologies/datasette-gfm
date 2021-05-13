from datasette import hookimpl
from datasette.utils.asgi import Response


def render_gfm(rows):
    return Response.text(rows)


@hookimpl
def register_output_renderer():
    return {"extension": "md", "render": render_gfm}

