from pprint import pprint
table = [[float(i) for i in line.split()] for line in open('data.txt')]
pprint(table)
