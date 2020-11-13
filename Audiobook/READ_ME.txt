Personalized Audiobook 

1. Store the PDF file to be read in the same folder as the main.py and paste the file name in the first set of single quotes. 
2. There are 2 packages to be installed.
	(i) import pyytsx3 - is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.  
	
	Installation - "pip install pyttsx3" 
		If you receive errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.
	
	Usage :
		import pyttsx3
		engine = pyttsx3.init()
		engine.say("I will speak this text")
		engine.runAndWait()

	Reference: https://pypi.org/project/pyttsx3/

	(ii) import PyPDF2 - A Pure-Python library built as a PDF toolkit. 
	
It is capable of:
•	extracting document information (title, author, …)
•	splitting documents page by page
•	merging documents page by page
•	cropping pages
•	merging multiple pages into a single page
•	encrypting and decrypting PDF files

By being Pure-Python, it should run on any Python platform without any dependencies on external libraries. It can also work entirely on StringIO objects rather than file streams, allowing for PDF manipulation in memory. It is therefore a useful tool for websites that manage or manipulate PDFs.
