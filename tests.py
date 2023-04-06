from huggingface import HFDataset
import logging

def test_create_dataset():

    hf_dataset = HFDataset()
    result = hf_dataset.create_dataset()

    assert result is not None
    for split in ["train", "test", "valid"]:
        assert split in result.keys()
