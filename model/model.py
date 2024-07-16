"""
The `Model` class is an interface between the ML model that you're packaging and the model
server that you're running it on.

The main methods to implement here are:
* `load`: runs exactly once when the model server is spun up or patched and loads the
   model onto the model server. Include any logic for initializing your model, such
   as downloading model weights and loading the model into memory.
* `predict`: runs every time the model server is called. Include any logic for model
  inference and return the model output.

See https://truss.baseten.co/quickstart for more.
"""
from .src.test_scene import TestScene


class Model:
    def __init__(self, **kwargs):
        # Uncomment the following to get access
        # to various parts of the Truss config.

        # self._data_dir = kwargs["data_dir"]
        # self._config = kwargs["config"]
        # self._secrets = kwargs["secrets"]
        self._model = None

    def load(self):
        # Load model here and assign to self._model.
        self._modal = TestScene()

    def predict(self, model_input):
        # Run model inference here
        action = model_input["action"]
        input = model_input["input"]
        if action=="echo_name":
            return self._modal.echo_name(input)
        if action == "odd_even":
            return self._modal.odd_even(input)
        if action == "download":
            file_id = model_input["file_id"]
            return self._modal.download(file_id)

