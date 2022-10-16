from pickle import TRUE
from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication


ws = Workspace.from_config()
print(ws)

print("Found workspace {} at location {}".format(ws.name, ws.location))