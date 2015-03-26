#! /usr/bin/python
try:
	import xml.etree.cElementTree as ET
except ImportError, e:
	import xml.etree.ElementTree as ET

testConfigXmlName = "tests.xml"

def Parse(xmlname):
	tree = ET.parse(xmlname)
	alltests = []
	testMatrix={}
	for cycle in tree.iterfind('cycles/cycle'):
		cyclename = cycle.attrib['name']
		testlist = []
		for test in cycle.iterfind('test'):
			testlist.append(test.text)
		testMatrix[cyclename]=testlist
	
	for c in testMatrix:
		for tname in testMatrix[c]:
				thatcase = tree.find('tests/test[@name=' + '"' + tname +'"' + ']')
				if thatcase != None:
					testcmd = thatcase[0].text
					testowner = thatcase[1].text
				test = {
					"enabled" : 'true',
					"owner" : testowner,
					"testgroup" : c,
					"testcase" : tname
				}
				alltests.append(test)
	return alltests


def GenerateTestPropertiesFile():
	configstring = "enableField=enabled\ngroupBy=testgroup\nfieldSeparator=.\nshowFields=testcase\nmultiplicityField=multiplicity"
	out = Parse(testConfigXmlName)
	out = out.__str__().replace("'true'","true")
	out = 'tests=' + out
	out = out + '\n' + configstring
	with open('tests.properties','w') as ff:
		ff.write(out)

GenerateTestPropertiesFile()

