import os
import argparse
from functools import reduce
from typing import List

def parse_graph(lines: List[str]):
    strippeds = [line.lstrip() for line in lines]
    filtereds: List[str] = filter(lambda line: line and line[0] != '#', strippeds)
    compacteds = [line.replace('\n', ' ') for line in filtereds]
    return reduce(lambda line1, line2: line1 + line2, compacteds)

def parse_graph_entry(graph: str) -> str:
	with open(graph) as f:
		fname: str = os.path.basename(graph).split('.')[0]
		return """	{ """ + f'"{fname}", R"({parse_graph(f.readlines())})"' + """},
"""

def main():
	parser = argparse.ArgumentParser(description = 'Generate embeddable mediapipe graph definition C/C++ headers')
	parser.add_argument('graphs',
						metavar='N',
						type= str,
						nargs='+',
						help='Graph File Paths'
	)
	args = parser.parse_args()
	header = """#pragma once

#include<map>
#include<string>

static const std::map<std::string, std::string> config_map
{
""" + str.join('\n', map(parse_graph_entry, args.graphs)) + """
};
	"""
	print(header)

if __name__ == '__main__':
	main()