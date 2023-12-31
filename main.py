#!/usr/bin/env python3

from anyserver import AnyServer

from examples.basic.status import router as STATUS_ROUTES
from examples.htmx.todo import TODO_ROUTES
from tests import TEST_ROUTES

# Declare the server instance and register all the routes
app = AnyServer(prefers='FastAPI')
app.static("./public")
app.register(STATUS_ROUTES)
app.register(TEST_ROUTES)
app.register(TODO_ROUTES)


def main():
    app.start()


if __name__ == '__main__':
    main()
