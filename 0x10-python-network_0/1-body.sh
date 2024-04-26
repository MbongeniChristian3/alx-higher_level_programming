#!/bin/bash

[ $# -eq 1 ] && { curl -s -o temp.txt -w "%{http_code}" "$1" | tail -n1 | grep -q '^200$' && cat temp.txt; } || echo "Usage: $0 <URL>"; rm -f temp.txt
