_Z='./program'
_Y='program'
_X='Error Please Install gcc'
_W='not find'
_V='Error! Please Install subprocess Library'
_U='pip install subprocess'
_T='Error! Please Install ruby_to_python Library'
_S='pip install ruby_to_python'
_R='Error! Please Install php2py Library'
_Q='pip install php2py'
_P='Error In Connecting To JVM'
_O='Error! Please Install py4j Library'
_N='pip install py4j'
_M='Error! Please Install Js2Py Library'
_L='pip install js2py'
_K='</title>'
_J='<title>'
_I='400x400'
_H='error'
_G='program.c'
_F='gcc'
_E='w+'
_D='tmp.js'
_C=True
_B='tmp.py'
_A='cls || clear'
import os
from tkinter import*
def convert_py_to_c(code):
	A='tmp.c'
	try:
		f=open(_B,_E);f.write(code);f.close();os.system('cython tmp.py');os.system(_A);cpyout=open(A).read()
		try:os.remove(_B);os.remove(A)
		except:pass
		return cpyout
	except:return _H
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
def convert_html_to_py(code,geometry=_I):
	code=code.replace("'''",'"""')
	try:title=code.split(_J)[1];title=title.split(_K)[0]
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
		os.system('python -m metapensiero.pj  || pip install javascripthon');f=open(_B,_E);f.write(code);f.close();os.system(f"python -m metapensiero.pj  tmp.py");os.system(_A);js=open(_D).read()
		try:os.remove(_B);os.remove(_D)
		except:pass
		return js
	except:return _H
def convert_js_to_py(code):
	try:
		try:from js2py import translate_file
		except:
			os.system(_L);os.system(_A)
			try:from js2py import translate_file
			except:print(_M);exit()
		f=open(_D,_E);f.write(code);f.close();translate_file(_D,_B);py=open(_B).read()
		try:os.remove(_B);os.remove(_D)
		except:pass
		return py
	except:return _H
def convert_py_to_java(code):
	try:from py4j.java_gateway import JavaGateway
	except:
		os.system(_N);os.system(_A)
		try:from py4j.java_gateway import JavaGateway
		except:print(_O);exit()
	try:gateway=JavaGateway()
	except:print(_P);exit()
	python_code=gateway.jvm.org.python.util.PythonInterpreter.javaToPython(code);return python_code
def convert_php_to_py(code):
	try:from php2py import transpile_code
	except:
		os.system(_Q);os.system(_A)
		try:from php2py import transpile_code
		except:print(_R);exit()
	python_code=transpile_code(code);return python_code
def convert_ruby_to_py(code):
	try:import ruby_to_python
	except:
		os.system(_S);os.system(_A)
		try:import ruby_to_python
		except:print(_T);exit()
	python_code=ruby_to_python.convert(code);return python_code
def convert_c_to_python(code):
	try:import subprocess
	except:
		os.system(_U);os.system(_A)
		try:import subprocess
		except:print(_V);exit()
	gd=subprocess.run([_F],capture_output=_C,text=_C)
	if _W in gd.lower():print(_X);exit()
	with open(_G,'w')as file:file.write(code)
	subprocess.run([_F,_G,'-o',_Y]);result=subprocess.run([_Z],capture_output=_C,text=_C);return result.stdout
def run_html(code,geometry=_I):
	try:from tkhtmlview import HTMLLabel
	except:
		import os;os.system('pip install tkhtmlview');os.system('clear || cls')
		try:from tkhtmlview import HTMLLabel
		except:print('Error! Please Install tkhtmlview Library');exit()
	try:title=code.split(_J)[1];title=title.split(_K)[0]
	except:title='ALIOL'
	root=Tk();root.title(title);root.geometry(geometry);my_label=HTMLLabel(root,html=f"\n{code}\n");my_label.pack(pady=20,padx=20);root.mainloop()
def run_python(code):exec(code)
def run_js(code):
	try:from js2py import translate_file
	except:
		os.system(_L);os.system(_A)
		try:from js2py import translate_file
		except:print(_M);exit()
	f=open(_D,_E);f.write(code);f.close()
	try:translate_file(_D,_B)
	except:print('Error In Converting Js code To Py Code!');exit()
	py=open(_B).read();exec(py)
def run_java(code):
	try:from py4j.java_gateway import JavaGateway
	except:
		os.system(_N);os.system(_A)
		try:from py4j.java_gateway import JavaGateway
		except:print(_O);exit()
	try:gateway=JavaGateway()
	except:print(_P);exit()
	exec(gateway.jvm.org.python.util.PythonInterpreter.javaToPython(code))
def run_php(code):
	try:from php2py import transpile_code
	except:
		os.system(_Q);os.system(_A)
		try:from php2py import transpile_code
		except:print(_R);exit()
	exec(transpile_code(code))
def run_ruby(code):
	try:import ruby_to_python
	except:
		os.system(_S);os.system(_A)
		try:import ruby_to_python
		except:print(_T);exit()
	exec(ruby_to_python.convert(code))
def run_c(code):
	try:import subprocess
	except:
		os.system(_U);os.system(_A)
		try:import subprocess
		except:print(_V);exit()
	gd=subprocess.run([_F],capture_output=_C,text=_C)
	if _W in gd.lower():print(_X);exit()
	with open(_G,'w')as file:file.write(code)
	subprocess.run([_F,_G,'-o',_Y]);result=subprocess.run([_Z],capture_output=_C,text=_C);exec(result.stdout)
