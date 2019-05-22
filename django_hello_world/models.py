import sys

from django.db import models

import natural_keys


if "loaddata" in sys.argv or "dumpdata" in sys.argv:
    MODEL_CLASS = natural_keys.NaturalKeyModel  # type: models.Model
else:
    MODEL_CLASS = models.Model


class Model(MODEL_CLASS):
    class Meta:
        abstract = True
