import datasets
from datasets import Dataset, DatasetDict
import pandas as pd
import fire

class HFDataset(object):
    """Simple class to create HF datasets."""

    def create_dataset(
        input_path: str = "/tmp",
        language: str = "en"
    ) -> pd.DataFrame:

        splits = ["train", "test", "valid"]
        dataset = DatasetDict()

        for split in splits:
            df = pd.read_csv(
                f"/tmp/insuranceqa_{split}.txt",
                names = [
                    "index",
                    "topic_en",
                    "question_zh",
                    "question_en",
                    "topic_zh"
                ],
                sep = "\t",
                engine = "python",
                header = 1
            )

            if language == "en":
                df = df.loc[:, ["index", "topic_en", "question_en"]]

            dataset[split] = Dataset.from_pandas(df)


        dataset.save_to_disk("./dataset")

    def create_answers_dataset(
        input_path: str = "/tmp",
        language: str = "en"
    ) -> pd.DataFrame:

        splits = ["train"]
        dataset = DatasetDict()

        for split in splits:
            df = pd.read_json(f"{input_path}/answers.json", orient = "index")

            if language == "en":
                df = df.loc[:, [language, "domain", "answers"]]

            dataset[split] = Dataset.from_pandas(df)


        dataset.save_to_disk("./dataset")

    def push_to_hub(input_path: str = "./dataset"):

        dataset = datasets.load_from_disk("./dataset")
        dataset.push_to_hub("insurance-qa-en")

if __name__ == "__main__":
    fire.Fire(HFDataset)
