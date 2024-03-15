# Importing In Python Project
```
E='ALIOL.py';B=exit;A=print;from os import system as F,listdir as G
if not E in G():
	try:from requests import get
	except:
		F('pip install requests')
		try:from requests import get
		except:A('Error! Please Install Requests Library');B()
	try:
		C=get('https://mr-r0ot.github.io/ALIOL_Python_Library/ALIOL.py')
		if C.status_code!=200:A('GiHub Error!');B()
	except:A('NetWork Error!');B()
	D=open(E,'w+');D.write(C.text);D.close()
from ALIOL import ALIOL
```

# Run Codes And Convert Codes By AI (need to internet)
```
---> More powerful but less speed and more restrictions


Converting:
	ALIOL.Convert_languages_code_AI(input_language,output_language,code,log=False)
    Exam:
	output=ALIOL.Convert_languages_code_AI('python','php',code='print("Hello World!")'    ,log=True)
	print(output)



Running:
	ALIOL.Run_languages_code_AI(language,code,log=False)
    Exam(running ruby code):
	ALIOL.Run_languages_code_AI('ruby',code='puts "hello"',    log=True)


```



# Run Codes And Convert Codes By Mechanical conversion (not need to internet)
```
---> Less power but more speed and less restrictions


ALIOL.run_ruby(code)
ALIOL.run_php(code)
ALIOL.run_java(code)
ALIOL.run_js(code)
ALIOL.run_python(code)
ALIOL.run_c(code)
ALIOL.run_html(code,geometry="400x400")


ALIOL.convert_ruby_to_py(code)
ALIOL.convert_php_to_py(code)
ALIOL.convert_py_to_java(code)
ALIOL.convert_py_to_js(code)
ALIOL.convert_js_to_py(code)
ALIOL.convert_html_to_py(code,geometry="400x400")
ALIOL.convert_py_to_html(code,lang='en',title)
ALIOL.convert_c_to_python(code)
ALIOL.convert_py_to_c(code)_python(code)
```





Coded By NICOLA (Telegram : @black_nicola)
