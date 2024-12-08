import os
import re
from collections import defaultdict
from PIL import Image
import time
from threading import Thread
import argparse

extensions_regex  = "\\.((jpg)|(jpeg)|(png))$"

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stats", action='store_true')
parser.add_argument("-v", "--verbose", action='store_true')
parser.add_argument("-t", "--threads", type=int, default=1)

args = parser.parse_args()

class Stats:
	def __init__(self, workers):
		self.workers = workers
		self.queue_size = 0
		self.runtime = 0.0
		pass

def get_files(d):
	return [f"uploads/{file}" for file in os.listdir(d) if re.search(extensions_regex, file.lower())]	

def get_original_files() -> list[str]:
	return get_files('./uploads')

def get_target_sizes():
	return [d for d in os.listdir("img") if re.search("[1-9][0-9]+", d)]

def resize_image(target: str, file: str) -> Image.Image:
	with Image.open(file) as im:
		w, h = im.size
		aspect = w / h

		return im.resize((int(aspect*int(target)), int(target)))


def save_to_target(target: str, im: Image.Image, name: str):
	print(f"saving to {name}")
	filename = name.split("/")[1]
	im.save(f"img/{target}/{filename}", quality=100, subsampling=0)

# for each file in targets, create a dict that tells you which file needs to go where
def create_targets():
	originals = set(get_original_files())
	print(originals)
	targets = get_target_sizes()
	print(targets)

	work_queue = []

	for target in targets:
		# list all the files in this target
		work_queue +=[(target, f) for f in list(originals - set(get_files(f"img/{target}")))]

	return work_queue

def thread_worker(name, queue):
	while queue:
		target, file = queue.pop()
		im = resize_image(target, file)
		save_to_target(target, im, file)
		if args.verbose:
			print(name, target, file)

def main():
	start = time.time()
	stats = Stats(args.threads)
	threads = []
	for i in range(args.threads):
		queue = create_targets()

		stats.queue_size = len(queue)

		t = Thread(target=thread_worker, args=[f"worker{i}", queue])
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	stats.runtime = time.time() - start

	if args.stats:
		print(f"Finished in {stats.runtime} seconds")
		print(f"{stats.workers} workers, {stats.queue_size} images")
		print(f"{stats.runtime/stats.queue_size} seconds per image")

if __name__ == "__main__":
	main()
