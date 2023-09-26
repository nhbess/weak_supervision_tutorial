import os

from collections import Counter
from nltk.corpus import stopwords

import numpy as np

import spacy
from spacy.training import Corpus
from spacy.tokens import Span


def load_data_split(split="train", all_labels=["DET"], subset=None):
    part3_path = ""

    # Path to the dataset file
    data_path = os.path.join("corpus", "UD_English-EWT")

    # Create a blank spacy pipeline
    nlp = spacy.blank("xx")
    reader = Corpus(os.path.join(data_path, f"{split}.spacy"))
    data = list(reader(nlp))
    if isinstance(subset, int):
        data = data[:subset]

    # Toy example: use a subset
    docs = [doc.reference.copy() for doc in data]

    # Set the gold labels
    for doc in docs:
        ents = []
        tok_pos = []
        for tok in doc:
            if tok.pos_ in all_labels:
                # print(tok.pos_)
                tok_pos.append(tok.pos_)
                ents.append(Span(doc, tok.i, tok.i + 1, tok.pos_))
            else:
                tok_pos.append("X")
        doc.set_ents(ents)
    return docs


def tag_all(docs, lfs):
    for doc in docs:
        for lf in lfs:
            doc = lf(doc)
    return docs


NOUN, VERB, ADJ, ADV, PRON, DET, PREP, ADP, NUM, CONJ, INTJ, PRT, PUNC, X, PROPN = \
    "NOUN", "VERB", "ADJ", "ADV", "PRON", "DET", "PREP", "ADP", "NUM", "CONJ", "INTJ", "PART", "PUNCT", "X", "PROPN"


# if nltk_pos == "DT":
#     yield token.i, token.i+1, "DET"
# elif nltk_pos == "CD":
#     yield token.i, token.i+1, "NUM"
# elif nltk_pos == "NNP" or nltk_pos == "NNPS":
#     yield token.i, token.i+1,"PROPN"
# elif nltk_pos == "JJ" or nltk_pos == "JJR" or nltk_pos == "JJS":
#     yield token.i, token.i+1, "ADJ"
# elif nltk_pos == "NN" or nltk_pos == "NNS":
#     yield token.i, token.i+1, "NOUN"
# elif nltk_pos == "VB" or nltk_pos == "VBD" or nltk_pos == "VBG" or nltk_pos == "VBN" or nltk_pos == "VBP" or nltk_pos == "VBZ":
#     yield token.i, token.i+1, "VERB"


def penntreebank2universal(tag):
    """ Returns a (token, tag)-tuple with a simplified universal part-of-speech tag.
    """
    if tag.startswith(("NNP-", "NNPS-")):
        return "%s-%s" % (NOUN, tag.split("-")[-1])
    if tag in ("NN", "NNS", "NP"):
        return NOUN
    if tag in ("NNP", "NNPS"):
        return PROPN
    if tag in ("MD", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
        return VERB
    if tag in ("JJ", "JJR", "JJS"):
        return ADJ
    if tag in ("RB", "RBR", "RBS", "WRB"):
        return ADV
    if tag in ("PRP", "PRP$", "WP", "WP$"):
        return PRON
    if tag in ("DT", "PDT", "WDT", "EX"):
        return DET
    if tag in ("IN",):
        return PREP
    if tag in ("CD",):
        return NUM
    if tag in ("CC",):
        return CONJ
    if tag in ("UH",):
        return INTJ
    if tag in ("POS", "RP", "TO"):
        return PRT
    if tag in ("SYM", "LS", ".", "!", "?", ",", ":", "(", ")", "\"", "#", "$"):
        return PUNC
    return X


def compute_recall_num_conflicts(docs):
    recalls, num_conflicts = [], []

    for doc in docs:

        recalls, num_conflicts = [], []
        doc_conflicts = {}
        for name, val in doc.spans.items():
            for v in val:
                for i in range(v.start, v.end):
                    if i in doc_conflicts:
                        doc_conflicts[i].append(v.label)
                    else:
                        doc_conflicts[i] = [v.label]

        doc_recall = len(doc_conflicts) / len(doc)
        doc_num_conflicts = np.where([len(set(v)) > 1 for v in doc_conflicts.values()])[0]
        doc_num_conflicts = len(doc_num_conflicts) / len(doc_conflicts) if len(doc_conflicts) > 0 else 0

        recalls.append(doc_recall)
        num_conflicts.append(doc_num_conflicts)

    recall = np.mean(recalls)
    num_conflicts = np.mean(num_conflicts)
    return recall, num_conflicts


def get_frequent_words(corpus, num_words):
    # Get all the words in the corpus
    words = [token.text.lower() for doc in corpus for token in doc if not token.is_punct]

    # Remove stopwords
    words = [w for w in words if w not in stopwords.words('english')]

    # Find the most frequent words
    word_freq = Counter(words)
    common_words = [w[0] for w in word_freq.most_common(num_words)]

    return common_words
