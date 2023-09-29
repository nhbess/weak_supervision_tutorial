import os
import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def load_raw_spam_dataset(load_train_labels: bool = False, split_dev_valid: bool = True):
    filenames = []
    path_to_data = os.path.join("data", "youtube", "raw")
    for name in os.listdir(path_to_data):
        if name.startswith("Youtube") and name.endswith(".csv"):
            filenames.append(os.path.join(path_to_data, name))
    filenames = sorted(filenames)

    dfs = []
    for i, filename in enumerate(filenames, start=1):
        df = pd.read_csv(filename)
        # Lowercase column names
        df.columns = map(str.lower, df.columns)
        # Remove comment_id field
        df = df.drop("comment_id", axis=1)
        # Add field indicating source video
        df["video"] = [i] * len(df)
        # Rename fields
        df = df.rename(columns={"class": "label", "content": "text"})
        # Shuffle order
        df = df.sample(frac=1, random_state=123).reset_index(drop=True)
        dfs.append(df)

    df_train = pd.concat(dfs[:4])

    # if train labels are unknown, fill the label column with default value
    if not load_train_labels:
        df_train["label"] = np.ones(len(df_train["label"])) * -1

    # pick up the remaining list of samples and split it into test and dev sets
    df_valid_test = dfs[4]
    df_dev, df_test = train_test_split(
        df_valid_test, test_size=250, random_state=123, stratify=df_valid_test.label
    )

    if split_dev_valid:
        return df_train, df_dev, df_test
    else:
        return df_train, df_test


from collections import Counter
def majority_vote(weak_annotations, num_classes=2, negative_class=0, default_class=1):
    labels = []
    for sample_annotation in weak_annotations:
        votes = Counter(sample_annotation)
        del votes[-1]
        winning_classes_votes = votes.most_common(num_classes)

        if len(winning_classes_votes) == 0:
            # if no LF matched
            winner_class = negative_class

        elif len(winning_classes_votes) > 1 and winning_classes_votes[0][1] == winning_classes_votes[1][1]:
            # a tie
            winner_class = default_class  # assign to default class
            winner_class = random.choice([winning_classes_votes[0][0], winning_classes_votes[1][0]]) # assign to random class

        else:
            # the simples case
            winner_class = winning_classes_votes[0][0]

        labels.append(winner_class)
    return np.array(labels)


if __name__ == '__main__':
    df_train, df_dev, df_valid, df_test = load_raw_spam_dataset(load_train_labels=True, split_dev_valid=True)
