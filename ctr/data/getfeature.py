feature_all = []
show_times = 0
lines = 0
for type_file in [".train.libfm", ".validation.libfm", ".test.libfm"]:
	with open("ml-tag/ml-tag" + type_file) as f:
		for line in f.readlines():
			feature_all.extend(line.split()[1:])
			lines += 1
		# print(len(feature_all))
		show_times += len(set(feature_all))
print("ml-tag", lines, len(feature_all), len(set(feature_all)))

# print(lines)
# print(len(feature_all))
# print(len(set(feature_all)))

feature_all = []
show_times = 0
lines = 0
for type_file in [".train.libfm", ".validation.libfm", ".test.libfm"]:
	with open("frappe/frappe" + type_file) as f:
		for line in f.readlines():
			feature_all.extend(line.split()[1:])
			lines += 1
		# print(len(feature_all))
		show_times += len(set(feature_all))
print("frappe", lines, len(feature_all), len(set(feature_all)))


feature_all = []
show_times = 0
lines = 0
for type_file in [".train.txt", ".valid.txt", ".test.txt"]:
	with open("FB15k/FB15k" + type_file) as f:
		for line in f.readlines():
			feature_all.extend(line.split()[1:])
			lines += 1
		# print(len(feature_all))
		show_times += len(set(feature_all))
print("FB15k", lines, len(feature_all), len(set(feature_all)))

feature_all = []
show_times = 0
lines = 0
for type_file in [".train.txt", ".valid.txt", ".test.txt"]:
	with open("WN18/WN18" + type_file) as f:
		for line in f.readlines():
			feature_all.extend(line.split()[1:])
			lines += 1
		# print(len(feature_all))
		show_times += len(set(feature_all))
print("WN18", lines, len(feature_all), len(set(feature_all)))
