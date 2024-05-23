from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion STAGE"
try:
    logger.info(f"Starting {STAGE_NAME}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e
