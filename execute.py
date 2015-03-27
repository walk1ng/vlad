#! /usr/bin/python
import os
import re
import json
try:
	import xml.etree.cElementTree as ET
except ImportError, e:
	import xml.etree.ElementTree as ET

tests = os.environ["alltests"]
testConfigXmlName = "tests.xml"

# retrieve test case
def RetrieveCase():
	cases_need_run = []
	cases = (re.sub('},{','}*{', tests[1:-1])).split('*')
	for c in cases:
		j = json.loads(c)
		casename = j.get('testcase','')
		tree = ET.parse(testConfigXmlName)
		casecmd = (tree.find('tests/test[@name=' + '"' + casename +'"' + ']'))[0].text
		case = {'name' : casename, 'cmd' : casecmd}
		cases_need_run.append(case)
	return cases_need_run


def Run(case):
	casename, casecmd = case['name'], case['cmd']
	print
	print "*" * 30
	print "TEST START: %s" % casename
	print "EXECUTE COMMAND: %s" % casecmd
	rtn = os.system(casecmd)
	result=""
	if rtn != 0:
		result = "FAILED"
	else:
		result = "PASS"
	print "TEST %s: %s" % (result, casename)
	print "*" * 30
	print
 
def ExecuteTest():
 	cases_need_run = RetrieveCase()
 	print "Below tests will be run:"
 	for c in cases_need_run:
 		print c['name']
 	print
 	for c in cases_need_run:
 		Run(c)

ExecuteTest()