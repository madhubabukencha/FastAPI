### Ways to Run server.py
We are using Dynaconf package to load configuration. 
- If you run `server.py` file directly, it will run the server by loading
  all the predefined settings or environment variables specified in Dynaconf.
- If you want to change `HOST` or `PORT` you can change it by running it
  on terminal:
  ``` bash
  python server.py --port 9999
  ```