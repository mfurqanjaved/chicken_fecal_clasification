from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion STAGE"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e




if __name__ == "__main__":
    try:
        logger.info(f"****************")
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> Stage: {STAGE_NAME} completed <<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e