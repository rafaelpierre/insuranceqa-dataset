
import requests
import logging
import fire
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://github.com/rafaelvp-db/word2vec-get-started/raw/master/corpus/insuranceqa/questions/{}.questions.txt"

def fetch_dataset(split: str = "train", download_path: str = "/tmp"):

    try:
        logger.info("Downloading Insurance QA dataset")
        response = requests.get(BASE_URL.format(split))
        with open(f"{download_path}/insuranceqa_{split}.txt", "w") as file:
            logger.info(f"Saving InsuranceQA dataset ({split}) to {download_path}...")
            file.write(response.text)

        sys.exit(0)

    except Exception as exception:
        logger.error(f"Error: {str(exception)}")
        sys.exit(-1)
    
if __name__ == "__main__":
    fire.Fire(fetch_dataset)

    

    