#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import sys
import re
import json

statements = []

filename = sys.argv[1]

# Open files as string
with open(filename) as inputFileHandle:
    file_string = inputFileHandle.read()

soup = BeautifulSoup(file_string, 'html.parser')

# First loop to get the names of all statements
for passage in soup.find_all("tw-passagedata"):
	statement = {}
	statement["id"] = int(passage.get('pid'))
	statement["name"] = str(passage.get('name'))

	statements.append(statement)

# Makes a copy of statements to iterate on later on
statements_copy = statements

# Second loop to link all statements together
statement_counter = 0
for statement in statements:
	statement_id = statement["id"]
	passage = soup.find("tw-passagedata", {"pid": statement_id})
	passage_text = passage.text
	statements[statement_counter]["body"] = passage_text.split('\n\n')[0]

	statements[statement_counter]["responses"] = []
	for brackets in re.findall("\[\[(.*?)\]\]", passage_text, flags=re.MULTILINE):
		answer = {}
		answer["user_inputs"] = []
		answer["user_inputs"].append(brackets.split('->')[0])
		answer_name = brackets.split('->')[1]
		# finds the id of the answser
		for statement_copy in statements_copy:
			if statement_copy["name"] == answer_name:
				answer_id = statement_copy["id"]

		answer["next_statement"] = answer_id
		
		statements[statement_counter]["responses"].append(answer)

	statement_counter += 1

with open('result.json', 'w') as fp:
	json.dump(statements, fp)
