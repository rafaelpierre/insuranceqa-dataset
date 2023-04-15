import pandas as pd

df = pd.read_json("/tmp/train.json", orient = "index")
print(df.columns)
print(df.loc[:, ["en", "domain", "answers"]].head())

with open("/tmp/answers.txt", "r") as file:
    answers_str = file.read()
    answers_str = answers_str.replace("++$++", "\t")

with open("/tmp/answers_parsed.txt", "w") as file:
    answers_str = answers_str.replace("++$++", "\t")
    file.write(answers_str)

df_answers = pd.read_csv(
    "/tmp/answers_parsed.txt",
    sep = "\t",
    engine = "python",
    names = ["answer_id", "answer_zh", "answer_en"],
    header = 0
)
print(df_answers.loc[:, ["answer_id", "answer_en"]].head())
