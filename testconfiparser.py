#! /usr/bin/python
try:
	import xml.etree.cElementTree as ET
except ImportError, e:
	import xml.etree.ElementTree as ET

testConfigXmlName = "tests.xml"


def Parse(xmlname):
	tree = ET.parse(xmlname)
	testMatrix={}
	for cycle in tree.iterfind('cycles/cycle'):
		cyclename = cycle.attrib['name']
		testlist = []
		for test in cycle.iterfind('test/name'):
			testlist.append(test.text)
		testMatrix[cyclename]=testlist
	tests= []
	for c in testMatrix:





def GenerateTestPropertiesFile():
	configstring = '''
					enableField=enabled
					groupBy=testgroup
					fieldSeparator=.
					showFields=testcase
					multiplicityField=multiplicity
					'''




