"""
This program shows how to take input from webpages.

Brief About StaticFiles
-----------------------
fastapi.staticfiles is a module in the FastAPI framework that
provides the StaticFiles class. This class allows you to easily serve
static files such as CSS files, JavaScript files, Images and fonts etc..,

When a request comes into your FastAPI application, FastAPI will check if the requested
path starts with /static. If it does, FastAPI will delegate the handling of that request
entirely to the mounted StaticFiles application. Your main FastAPI routes and logic will
not be involved in processing these requests.

- The "/static" part specifies the URL path prefix where this sub-application will be
  accessible. Any request that starts with /static will be routed to the StaticFiles
  instance for processing. 
- StaticFiles(directory="static") tells FastAPI to serve files from a directory named static
  (which should be in the same directory as your main Python file or accessible via a relative path)
- name="static" gives the mounted static files application the internal name "static"

Importance of Annotated
-----------------------
When a client sends a POST request to the /survey endpoint, the Form() annotation within
Annotated tells FastAPI to expect the name, happy, and talk parameters to be present in
the request body, specifically encoded as application/x-www-form-urlencoded data (typically
from an HTML form submission). FastAPI will then parse this data from the request body and
make it available as arguments to the survey function.

To access results
-----------------
http://127.0.0.1:8000/static/survey.html
"""
import logging
from http import HTTPStatus
from typing import Annotated

from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)

logging.info("Access Results at : http://127.0.0.1:8000/static/survey.html")
@app.post("/survey")
# Make sure these parameter names match with attributes in your html forms
def survey(name: Annotated[str, Form()],
           happy: Annotated[str, Form()],
           talk: Annotated[str, Form()]):
    logging.info("[Survey] name:%r, happy:%r, talk:%r", name, happy, talk)
    return RedirectResponse(
        url="/static/thanks.html",
        status_code=HTTPStatus.FOUND
    )
