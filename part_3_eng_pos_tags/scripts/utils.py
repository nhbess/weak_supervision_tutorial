import os

import spacy
from spacy.training import Corpus
from spacy.tokens import Span


def load_data_split(split="train", all_labels=["DET"], subset=None):
    part3_path = "part_3_eng_pos_tags"

    # Path to the dataset file
    data_path = os.path.join(part3_path, "corpus", "UD_English-EWT")

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


NOUN, VERB, ADJ, ADV, PRON, DET, PREP, ADP, NUM, CONJ, INTJ, PRT, PUNC, X = \
    "NOUN", "VERB", "ADJ", "ADV", "PRON", "DET", "PREP", "ADP", "NUM", "CONJ", "INTJ", "PART", "PUNCT", "X"


def penntreebank2universal(tag):
    """ Returns a (token, tag)-tuple with a simplified universal part-of-speech tag.
    """
    if tag.startswith(("NNP-", "NNPS-")):
        return "%s-%s" % (NOUN, tag.split("-")[-1])
    if tag in ("NN", "NNS", "NNP", "NNPS", "NP"):
        return NOUN
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
