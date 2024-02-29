_g='The server blocked us! You have to change the system IP using VPNs or...'
_f='Please try after 24 hours.'
_e='/html/body/div/div/main/div[1]/div[3]/div[2]/div/div[2]/div'
_d='//*[@id="convert-btn"]'
_c='NetWork Error!'
_b='./program'
_a='program'
_Z='Error Please Install gcc'
_Y='not find'
_X='Error! Please Install subprocess Library'
_W='pip install subprocess'
_V='Error! Please Install ruby_to_python Library'
_U='pip install ruby_to_python'
_T='Error! Please Install php2py Library'
_S='pip install php2py'
_R='Error In Connecting To JVM'
_Q='Error! Please Install py4j Library'
_P='pip install py4j'
_O='Error! Please Install Js2Py Library'
_N='pip install js2py'
_M='</title>'
_L='<title>'
_K='400x400'
_J='error'
_I='//*[@id="input-text"]/textarea'
_H='program.c'
_G='gcc'
_F='w+'
_E='tmp.js'
_D='--headless'
_C='tmp.py'
_B=True
_A='cls || clear'
import os
from tkinter import*
def version():return'1.0.0'
def help():return'Coded By NICOLA (Telegram : @black_nicola)'
def convert_py_to_c(code):
	A='tmp.c'
	try:
		f=open(_C,_F);f.write(code);f.close();os.system('cython tmp.py');os.system(_A);cpyout=open(A).read()
		try:os.remove(_C);os.remove(A)
		except:pass
		return cpyout
	except:return _J
def convert_py_to_html(code,lang='en',title='ALIOL'):out=f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
   <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
   <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head><body>
<py-script>
{code}
</py-script>
</body></html>''';return out
def convert_html_to_py(code,geometry=_K):
	code=code.replace("'''",'"""')
	try:title=code.split(_L)[1];title=title.split(_M)[0]
	except:title='py_to_html AI'
	out=f"""
from tkinter import *
try:
    from tkhtmlview import HTMLLabel
except:
    import os
    os.system('pip install tkhtmlview')
    os.system('clear || cls')
    from tkhtmlview import HTMLLabel
root = Tk()
root.title(\" {title} \")
root.geometry(\"{geometry}\")
my_label = HTMLLabel(root, html='''
{code}
''')
my_label.pack(pady=20, padx=20)
root.mainloop()""";return out
def convert_py_to_js(code):
	try:
		os.system('python -m metapensiero.pj  || pip install javascripthon');f=open(_C,_F);f.write(code);f.close();os.system(f"python -m metapensiero.pj  tmp.py");os.system(_A);js=open(_E).read()
		try:os.remove(_C);os.remove(_E)
		except:pass
		return js
	except:return _J
def convert_js_to_py(code):
	try:
		try:from js2py import translate_file
		except:
			os.system(_N);os.system(_A)
			try:from js2py import translate_file
			except:print(_O);exit()
		f=open(_E,_F);f.write(code);f.close();translate_file(_E,_C);py=open(_C).read()
		try:os.remove(_C);os.remove(_E)
		except:pass
		return py
	except:return _J
def convert_py_to_java(code):
	try:from py4j.java_gateway import JavaGateway
	except:
		os.system(_P);os.system(_A)
		try:from py4j.java_gateway import JavaGateway
		except:print(_Q);exit()
	try:gateway=JavaGateway()
	except:print(_R);exit()
	python_code=gateway.jvm.org.python.util.PythonInterpreter.javaToPython(code);return python_code
def convert_php_to_py(code):
	try:from php2py import transpile_code
	except:
		os.system(_S);os.system(_A)
		try:from php2py import transpile_code
		except:print(_T);exit()
	python_code=transpile_code(code);return python_code
def convert_ruby_to_py(code):
	try:import ruby_to_python
	except:
		os.system(_U);os.system(_A)
		try:import ruby_to_python
		except:print(_V);exit()
	python_code=ruby_to_python.convert(code);return python_code
def convert_c_to_python(code):
	try:import subprocess
	except:
		os.system(_W);os.system(_A)
		try:import subprocess
		except:print(_X);exit()
	gd=subprocess.run([_G],capture_output=_B,text=_B)
	if _Y in gd.lower():print(_Z);exit()
	with open(_H,'w')as file:file.write(code)
	subprocess.run([_G,_H,'-o',_a]);result=subprocess.run([_b],capture_output=_B,text=_B);return result.stdout
def run_html(code,geometry=_K):
	try:from tkhtmlview import HTMLLabel
	except:
		import os;os.system('pip install tkhtmlview');os.system('clear || cls')
		try:from tkhtmlview import HTMLLabel
		except:print('Error! Please Install tkhtmlview Library');exit()
	try:title=code.split(_L)[1];title=title.split(_M)[0]
	except:title='ALIOL'
	root=Tk();root.title(title);root.geometry(geometry);my_label=HTMLLabel(root,html=f"\n{code}\n");my_label.pack(pady=20,padx=20);root.mainloop()
def run_python(code):exec(code)
def run_js(code):
	try:from js2py import translate_file
	except:
		os.system(_N);os.system(_A)
		try:from js2py import translate_file
		except:print(_O);exit()
	f=open(_E,_F);f.write(code);f.close()
	try:translate_file(_E,_C)
	except:print('Error In Converting Js code To Py Code!');exit()
	py=open(_C).read();exec(py)
def run_java(code):
	try:from py4j.java_gateway import JavaGateway
	except:
		os.system(_P);os.system(_A)
		try:from py4j.java_gateway import JavaGateway
		except:print(_Q);exit()
	try:gateway=JavaGateway()
	except:print(_R);exit()
	exec(gateway.jvm.org.python.util.PythonInterpreter.javaToPython(code))
def run_php(code):
	try:from php2py import transpile_code
	except:
		os.system(_S);os.system(_A)
		try:from php2py import transpile_code
		except:print(_T);exit()
	exec(transpile_code(code))
def run_ruby(code):
	try:import ruby_to_python
	except:
		os.system(_U);os.system(_A)
		try:import ruby_to_python
		except:print(_V);exit()
	exec(ruby_to_python.convert(code))
def run_c(code):
	try:import subprocess
	except:
		os.system(_W);os.system(_A)
		try:import subprocess
		except:print(_X);exit()
	gd=subprocess.run([_G],capture_output=_B,text=_B)
	if _Y in gd.lower():print(_Z);exit()
	with open(_H,'w')as file:file.write(code)
	subprocess.run([_G,_H,'-o',_a]);result=subprocess.run([_b],capture_output=_B,text=_B);exec(result.stdout)
def Convert_languages_code_AI(input_language,output_language,code,log=False):
	libs=['selenium','requests']
	for l in libs:
		try:exec(f"import {l}")
		except:
			os.system(f"pip install {l}")
			try:exec(f"import {l}")
			except:print(f"Please Install {l}");sysexit()
	from selenium import webdriver;from selenium.webdriver.common.by import By;from time import sleep;from sys import exit as sysexit;from selenium.webdriver.firefox.options import Options as firefox_option_driver;firefox_option=firefox_option_driver();firefox_option.add_argument(_D);from selenium.webdriver.edge.options import Options as edge_option_driver;edge_option=edge_option_driver();edge_option.add_argument(_D);from selenium.webdriver.ie.options import Options as ie_option_driver;ie_option=ie_option_driver();ie_option.add_argument(_D);from selenium.webdriver.chrome.options import Options as chrome_option_driver;chrome_option=chrome_option_driver();chrome_option.add_argument(_D)
	try:driver=webdriver.Firefox()
	except:
		try:driver=webdriver.Edge(edge_option)
		except:
			try:driver=webdriver.Chrome(chrome_option)
			except:
				try:driver=webdriver.Safari()
				except:
					try:driver=webdriver.Ie(ie_option)
					except:
						if log==_B:print(f"\n    [ - ] Error: Webdriver File Not Find!\n    Please Download Chrome Or ... WebDriver File On Move To Path App")
						sysexit()
	def wait_full_xpath(xp):
		while _B:
			try:driver.find_element(By.XPATH,xp);break
			except:sleep(3)
	sleep(.5)
	try:driver.get(f"https://www.codeconvert.ai/{input_language}-to-{output_language}-converter")
	except:return _c
	wait_full_xpath(_I);driver.find_element(By.XPATH,_I).send_keys(code);sleep(1);driver.find_element(By.XPATH,_d).click();sleep(6);output=driver.find_element(By.XPATH,_e).text;driver.quit()
	if _f in output:return _g
	else:return output
def Run_languages_code_AI(language,code,log=False):
	from selenium import webdriver;from selenium.webdriver.common.by import By;from time import sleep;from sys import exit as sysexit;from selenium.webdriver.firefox.options import Options as firefox_option_driver;firefox_option=firefox_option_driver();firefox_option.add_argument(_D);from selenium.webdriver.edge.options import Options as edge_option_driver;edge_option=edge_option_driver();edge_option.add_argument(_D);from selenium.webdriver.ie.options import Options as ie_option_driver;ie_option=ie_option_driver();ie_option.add_argument(_D);from selenium.webdriver.chrome.options import Options as chrome_option_driver;chrome_option=chrome_option_driver();chrome_option.add_argument(_D)
	try:driver=webdriver.Firefox(firefox_option)
	except:
		try:driver=webdriver.Edge(edge_option)
		except:
			try:driver=webdriver.Chrome(chrome_option)
			except:
				try:driver=webdriver.Safari()
				except:
					try:driver=webdriver.Ie(ie_option)
					except:
						if log==_B:print(f"\n    [ - ] Error: Webdriver File Not Find!\n    Please Download Chrome Or ... WebDriver File On Move To Path App")
						sysexit()
	def wait_full_xpath(xp):
		while _B:
			try:driver.find_element(By.XPATH,xp);break
			except:sleep(3)
	sleep(.5)
	try:driver.get(f"https://www.codeconvert.ai/{language}-to-python-converter")
	except:return _c
	wait_full_xpath(_I);driver.find_element(By.XPATH,_I).send_keys(code);sleep(1);driver.find_element(By.XPATH,_d).click();sleep(6);output=driver.find_element(By.XPATH,_e).text;driver.quit()
	if _f in output:return _g
	else:exec(output)
