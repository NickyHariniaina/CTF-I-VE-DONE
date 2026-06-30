#!/bin/bash

while read line; do echo "$line" | python level4.py; done < flag.txt | grep -oP "picoCTF{.*}"
