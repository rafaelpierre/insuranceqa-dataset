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
                "/tmp/insuranceqa_train.txt",
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


        return dataset


if __name__ == "__main__":
    fire.Fire(HFDataset)
