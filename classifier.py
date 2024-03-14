from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Create a ClassificationModel
model = ClassificationModel(
    'bert',
    'bert-base-cased',
    num_labels=3,
)

# Make predictions with the model
predictions, raw_outputs = model.predict(["Sam was a Wizard"])
