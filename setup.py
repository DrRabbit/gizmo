from distutils.core import setup
import py2exe

setup(windows=[{"script": "GUI_2.py"}], options={"py2exe": {"includes": ["sip", "PyQt4"]}}, requires=['pyodbc',
                                                                                                      'numpy',
                                                                                                      'pandas'])
