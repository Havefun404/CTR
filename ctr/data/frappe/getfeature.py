feature_all = []
show_times = 0
lines = 0
for type_file in [".train.libfm", ".validation.libfm", ".test.libfm"]:
	with open("frappe" + type_file) as f:
		for line in f.readlines():
			feature_all.extend(line.split())
			lines += 1
		# print(len(feature_all))
		show_times += len(set(feature_all))
print(lines, len(feature_all), len(set(feature_all)))

# print(lines)
# print(len(feature_all))
# print(len(set(feature_all)))