import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        # 1. Use 'os' to get the dynamic path to the logs folder
        # This prevents errors if you run the project from a different location
        log_path = os.path.join(os.getcwd(), "logs", "automation.log")

        # 2. Configure Logging
        logging.basicConfig(filename=log_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)  # force=True creates the file if it doesn't exist

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
