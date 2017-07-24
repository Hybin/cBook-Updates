#! /bin/bash

# search the book
# the varible title is what you input
title={query}

# search the book based on title
curl 'http://chuangshi.qq.com/search/searchindex/type/all/wd/'$title'.html' > result.txt

# get the page address in result.txt
url=