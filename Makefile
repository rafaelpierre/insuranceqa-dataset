data:
	python insuranceqa.py --split=train
	python insuranceqa.py --split=test
	python insuranceqa.py --split=valid

push:
	python huggingface.py create_dataset
	python huggingface.py push_to_hub