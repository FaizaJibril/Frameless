"""Endpoints for getting version information."""
from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from ..schemas.base import VersionResponse
from ..version import __version__

base_router = APIRouter()


@base_router.get("/", response_class=HTMLResponse)
async def root(request: Request) -> Any:
    """Serve the main HTML page."""
    return """
    <html>
        <head>
            <title>Frameless API</title>
            <meta http-equiv="refresh" content="0; url=/static/index.html">
        </head>
        <body>
            <p>Redirecting to <a href="/static/index.html">Frameless Interface</a>...</p>
        </body>
    </html>
    """


@base_router.get("/version", response_model=VersionResponse)
async def version() -> Any:
    """Provide version information about the web service.

    \f
    Returns:
        VersionResponse: A json response containing the version number.
    """
    return VersionResponse(version=__version__)
