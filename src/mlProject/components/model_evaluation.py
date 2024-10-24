from pathlib import Path
from urllib.parse import urlparse

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from mlflow.models.signature import infer_signature
from sklearn.metrics import classification_report

from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, y_true, y_pred):
        # Initialize result dictionary
        results = {}

        # Precision, recall, and F1-score
        class_report = classification_report(
            y_true, y_pred, output_dict=True, zero_division=0
        )
        results["precision"] = class_report["macro avg"]["precision"]
        results["recall"] = class_report["macro avg"]["recall"]
        results["f1_score"] = class_report["macro avg"]["f1-score"]

        return results

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_labels = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_labels = model.predict(test_x)
            scores = self.eval_metrics(test_labels, predicted_labels)

            # Saving metrics as local
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("precision", scores["precision"])
            mlflow.log_metric("recall", scores["recall"])
            mlflow.log_metric("f1_score", scores["f1_score"])

            input_example = test_x[:2]
            signature = infer_signature(
                input_example, model.predict(input_example)
            )

            # Model registry does not work with file store,
            # it requires a tracking server with a backend store
            # (e.g., PostgreSQL, MySQL) to manage model versions,
            # their metadata, and transitions.

            registered_model_name = (
                "RandomForestModel"
                if tracking_url_type_store != "file"
                else None
            )

            # Register the model
            # There are other ways to use the Model Registry, which depends
            # on the use case, please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model",
                registered_model_name=registered_model_name,
                input_example=input_example,
                signature=signature,
            )
