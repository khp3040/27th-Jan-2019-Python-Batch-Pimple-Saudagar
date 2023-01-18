import json

with open('example_2.json', 'rb') as example:
    dataset = json.load(example)
    for key, value in dataset.iteritems():
        for key, value1 in value.iteritems():
            print key, value1
