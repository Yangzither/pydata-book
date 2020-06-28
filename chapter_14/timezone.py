import json
path = '../datasets/bitly_usagov/example.txt'
records = [json.loads(line) for line in open(path)]

# records = []
# for line in open(path):
#     records.append(json.loads(line))

print(len(records))
print(type(records))
#print(records)
#print(records[0])

# print(type(records[0]))
# print(records[0]['tz'])

timezones = []
for rec in records:
    if 'tz' in rec:
        timezones.append(rec['tz'])

print(type(timezones))
print(len(timezones))
print(timezones[0])
print(timezones[:10])

def counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] = counts[x] + 1
        else:
            counts[x] = 1
    return counts

time_counts = counts(timezones)
print(type(time_counts))

def top_counts(count_dict, n=10):
    value_key_pairs = [(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

top_counts1 = top_counts(time_counts)
print(top_counts1)
