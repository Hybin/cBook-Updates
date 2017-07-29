# cBook-Updates

[![author](https://img.shields.io/badge/Hybin-STU-red.svg)](https://github.com/Hybin)
[![Language](https://img.shields.io/badge/Python-3.5-yellow.svg)](https://www.python.org)
![Version](https://img.shields.io/badge/version-0.1-green.svg)
![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Download](https://img.shields.io/badge/downloads-87k-brightgreen.svg)](https://raw.githubusercontent.com/Hybin/cBook-Updates/master/cBook%20Updates.alfredworkflow)

This is a **workflow** for Alfred. In order to get the updating info of your favorite books, it would be an awesome tool for you to check the updating information and read the latest chapter(s) right now!

## Installation

* Download the [cBook Updates.alfredworkflow](https://raw.githubusercontent.com/Hybin/cBook-Updates/master/cBook%20Updates.alfredworkflow).

* Double-click and import it into Alfred 3.

## Configuaration

The **Script Filter** is based on Python 3 while Alfred 3 support Python 2.x only. In order to run it correctly, we may need to do something first.

First install Python 3 on your computer, then run shell:

	$ echo $PATH

and you will get something like this:

	/usr/bin:/usr/local/bin:/bin:/usr/sbin:/sbin:/Library/Frameworks/Python.framework/Versions/3.5/bin:

Now with the directory `/Library/Frameworks/Python.framework/Versions/3.5/bin`, you are able to find the exec `Python3.5`. 
* Click the Alfred 3 -> Preferences -> Workflows
* Click cBook Updates
* Double click Script Filter and you will see:

	function query {
	/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 - <<END
	import search
	search.query("{query}")
	END
	}
	query

Replace `/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5` with your own Python 3 path.

## Usage

The workflow requires constant internet connection.

`get {query}`: Input the book tilte as {query} with keyword `get`

## ScreenShot

![insert](https://github.com/Hybin/cBook-Updates/blob/master/screenshot/insert.png?raw=true)

![Get Results](https://github.com/Hybin/cBook-Updates/blob/master/screenshot/getResults.png?raw=true)

![Get Content](https://github.com/Hybin/cBook-Updates/blob/master/screenshot/getContent.png?raw=true)

## ChangeLog

####v0.1(2017-07-29)

* release version 0.1

## Copyright

The MIT License (MIT)

Copyright (c) 2016 [Hybin-Hwang](https://github.com/Hybin)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

