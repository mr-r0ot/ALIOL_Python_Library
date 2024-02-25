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
import ALIOL
```



# Commands
```
run_ruby(code)
run_php(code)
run_java(code)
run_js(code)
runALIOL.run_ruby(code)
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
run_c(code)
run_html(code,geometry="400x400")


convert_ruby_to_py(code)
convert_php_to_py(code)
convert_py_to_java(code)
convert_py_to_js(code)
convert_js_to_py(code)
convert_html_to_py(code,geometry="400x400")
convert_py_to_html(code,lang='en',title)
convert_c_to_python(code)
convert_py_to_c(code)
```





Coded By NICOLA (Telegram : @black_nicola)
