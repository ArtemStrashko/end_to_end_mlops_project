from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import (
    DataTransformationTrainingPipeline,
)
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(">>>>>> stage %s started <<<<<<", STAGE_NAME)
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(">>>>>> stage %s started <<<<<<", STAGE_NAME)
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(">>>>>> stage %s started <<<<<<", STAGE_NAME)
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(">>>>>> stage %s started <<<<<<", STAGE_NAME)
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"
try:
    logger.info(">>>>>> stage %s started <<<<<<", STAGE_NAME)
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.main()
    logger.info(">>>>>> stage %s completed <<<<<<\n\nx==========x", STAGE_NAME)
except Exception as e:
    logger.exception(e)
    raise e
