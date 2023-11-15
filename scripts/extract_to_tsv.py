#extract_to_tsv.py
import json
import csv
import random
from pathlib import Path
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-o", "--output", required=True, help="the input json file name"
)
# Add an argument without prefix
parser.add_argument('json_file', nargs='?', default='mcgill.json',help='Input json file placed in the data folder')
parser.add_argument('num_posts_to_output', nargs='?', default=50,help='Input json file placed in the data folder')
args = parser.parse_args()
# print(args)

cd=Path.cwd()
pd=cd.parent
input_file=pd/'data'/args.json_file
output_file=pd/'data'/args.output
# print(input_file)

# mcgill='../data/mcgill.json'
# concordia='../data/concordia.json'

with open (input_file,'r') as f:
    data=json.load(f)

info=[]
for i in data['data']['children']:
    info.append((i['data']['name'],i['data']['title'],))

# print(len(info))
random.shuffle(info)
n=int(args.num_posts_to_output)
# print(n)
if (n<len(info)):
    info=info[:n]

with open(output_file, 'w', newline='') as tsvfile:
    # Create a CSV writer with tab as the delimiter
    tsv_writer = csv.writer(tsvfile, delimiter='\t')

    # Write the header
    tsv_writer.writerow(['Name', 'Title', 'coding'])

    # Write the zipped data
    tsv_writer.writerows(info)
