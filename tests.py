from huggingface import HFDataset
import logging

def test_create_dataset():

    hf_dataset = HFDataset()
    hf_dataset.create_dataset()
