Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
b = lambda x:X[0]=="a"
b("apple")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b("apple")
  File "<pyshell#0>", line 1, in <lambda>
    b = lambda x:X[0]=="a"
NameError: name 'X' is not defined. Did you mean: 'x'?
b = lambda x:x[0]=="a"
b("apple")

True

c= lambda x: "even nmber" if x%2==0 else "odd"
c(6)
'even nmber'
