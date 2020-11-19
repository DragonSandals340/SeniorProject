# gbAPI

A REST API using the FAST API framework to handle the user system for the gameboards, along with updating gameboard moves.

## Getting Started

To create a new virtual environment:
```
python -m venv yourVirtualEnvName
```

To activate your virtual environment in windows powershell:
```
yourVirtualEnvName\Scripts\activate.ps1
```

To activate in OSX / Unix:
```
source yourVirtualEnvName/bin/activate
```


Once the virtual environment is created, then install the requirements and gbAPI package itself.
```
pip install -r requirements.txt
pip install -e .
```

Once this is done you are set to use gbAPI!

## Usage

Now that gbAPI is installed, the REST API can easily be started by calling the simple command `gbAPI`. Running this will initialize the uvicorn server and the REST API will be ready to go!

To explore the Fast API docs - go to the following url: host/docs.

By default, local host is setup as the host / port. So view the docs using the following link http://127.0.0.1/docs#/