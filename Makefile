python = /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

testmarker: test_roman.py roman.py
	$(python) test_roman.py
	touch testmarker


