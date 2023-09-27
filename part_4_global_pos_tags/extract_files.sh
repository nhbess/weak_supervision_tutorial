#!/bin/bash

#wget https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-3105/ud-treebanks-v2.5.tgz

mkdir -p assets
mv ud-treebanks-v2.5.tar assets/
tar xf assets/ud-treebanks-v2.5.tar -C assets/
