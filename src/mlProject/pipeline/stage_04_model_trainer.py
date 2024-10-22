from mlProject import logger
from mlProject.components.model_trainer import ModelTrainer
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == "__main__":
    try:
        logger.info(">>>>>> stage %s started <<<<<<", STAGE_NAME)
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(
            ">>>>>> stage %s completed <<<<<<\n\nx==========x", STAGE_NAME
        )
    except Exception as e:
        logger.exception(e)
        raise e
