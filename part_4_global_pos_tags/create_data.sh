#!/bin/bash

# specify the treebank
vars_ud_treebank="UD_English-ESL"

# train data
python scripts\copy_files.py train conllu assets\ud-treebanks-v2.5\UD_English-ESL\ corpus\UD_English-ESL\train\
python -m spacy convert corpus\UD_Spanish-GSD\train\ corpus\UD_Spanish-GSD\ --converter conllu -n 1 -T -C

# dev data
python scripts\copy_files.py test conllu assets\ud-treebanks-v2.5\UD_English-ESL\ corpus\UD_English-ESL\test\
python -m spacy convert corpus\UD_Spanish-GSD\test\ corpus\UD_Spanish-GSD\ --converter conllu -n 1 -T -C
