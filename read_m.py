data = []
count = 0
words_len = 0

with open('reviews.txt', 'r') as file:
	for message in file:
		data.append(message.strip())
		#count += 1
		#if count % 1000 == 0:
		#	print(len(data))
			
print("finish reading. there is", len(data))

for d in data:
	words_len += len(d)
	if len(d) < 100:
		print(d, "\n")

print("average = ", words_len / len(data))