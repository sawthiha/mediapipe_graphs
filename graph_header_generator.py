import os
import argparse
from functools import reduce
from typing import List

def if_not_comment_or_empty(line: str) -> bool:
    stripped = line.lstrip()
    return stripped and stripped[0] != '#'

def parse_graph(lines: List[str]):
    filtereds: List[str] = filter(if_not_comment_or_empty, lines)
    return reduce(lambda line1, line2: line1 + line2, filtereds)

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
	graphs = args.graphs
	graphs.reverse()
	header = """#pragma once

#include<unordered_map>
#include<string>

static const std::unordered_map<std::string, std::string> config_map
{
""" + str.join('\n', map(parse_graph_entry, graphs)) + """
};
	"""
	print(header)

if __name__ == '__main__':
	main()