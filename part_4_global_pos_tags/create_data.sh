#!/bin/bash

# specify the treebank
vars_ud_treebank=UD_English-EWT

# train data
python scripts/copy_files.py train conllu assets/ud-treebanks-v2.5/${vars_ud_treebank}/ corpus/${vars_ud_treebank}/train/
python -m spacy convert corpus/${vars_ud_treebank}/train/ corpus/${vars_ud_treebank}/ --converter conllu -n 1 -T -C

# dev data
python scripts/copy_files.py test conllu assets/ud-treebanks-v2.5/${vars_ud_treebank}/ corpus/${vars_ud_treebank}/test/
python -m spacy convert corpus/${vars_ud_treebank}/test/ corpus/${vars_ud_treebank}/ --converter conllu -n 1 -T -C
