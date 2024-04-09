Try it out:

```
$ python3 -m venv plugin-python/.venv
$ source plugin-python/.venv/bin/activate
$ pip install -r plugin-python/requirements.txt
$ bazel help
2024-04-09T14:41:52.873-0700 [INFO]  hello-world: running hello-world plugin from plugin-python/launch.sh
Aspect CLI is a better frontend for running bazel
...
Custom Commands from Plugins:
  custom_from_python custom command written in python
```
