from PIL import Image
import os

pics = [p for p in os.listdir() if p.lower().endswith('.jpg') or p.lower().endswith('.jpeg') or p.lower().endswith('.png')]

results = []

for p in pics:
	im = Image.open(p)
	width, height = im.size
	im.close()

	results.append((p, width / height))

	# print(f"{{filename: '{p}', aspectRatio: {width / height}}},")

from_a6000 = [p for p in results if p[0].lower().startswith("dsc")]
from_a6600_1 = [p for p in results if p[0].lower().startswith("b")]
from_a6600_2 = [p for p in results if not (p[0].lower().startswith("dsc") or p[0].lower().startswith("b"))]


from_a6000.sort()
from_a6000.reverse()

from_a6600_1.sort()
from_a6600_1.reverse()

from_a6600_2.sort()
from_a6600_2.reverse()

print('[')

final_ordering = from_a6600_2 + from_a6600_1  + from_a6000

for i in range(len(final_ordering)):
	print(f"{{\"filename\": \"{final_ordering[i][0]}\", \"aspectRatio\": {final_ordering[i][1]}}}", end="")
	if i != len(final_ordering) - 1:
		print(",")

print(']')