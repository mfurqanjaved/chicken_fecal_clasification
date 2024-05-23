from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier import logger
from cnnClassifier.components.data_ingestion import DataIngestion


STAGE_NAME = "Data Ingestion STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.exception(e)
        raise e
