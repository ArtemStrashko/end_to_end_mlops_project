import os

import pandas as pd
from sklearn.model_selection import train_test_split

from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: You can add different data transformation techniques
    # such as Scaler, PCA and all. You can perform all kinds of EDA
    # in ML cycle here before passing this data to the model.

    # I am only adding train_test_spliting cz this data is already cleaned up

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Shuffle the data
        data = data.sample(frac=1, random_state=42).reset_index(drop=True)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data, train_size=0.75, random_state=42)

        train.to_csv(
            os.path.join(self.config.root_dir, "train.csv"), index=False
        )
        test.to_csv(
            os.path.join(self.config.root_dir, "test.csv"), index=False
        )

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
