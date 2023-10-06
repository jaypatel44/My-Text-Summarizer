from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.conponents.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        logger.info("Config")
        data_ingestion_config = config.get_data_ingestion_config()
        logger.info("get_data_ingestion_config")
        data_ingestion = DataIngestion(config=data_ingestion_config)
        logger.info("Downloading....")
        data_ingestion.download_file()
        logger.info("Downloaded yaaaaaa......")
        data_ingestion.extract_zip_file()
