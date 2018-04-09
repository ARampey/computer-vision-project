# python download_images.py --urls urls.txt --output images/face

from imutils import paths
import argparse
import requests
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--urls", required=True,
	help="path to file containing image URLs")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory of images")
args = vars(ap.parse_args())

# grab the list of URLs from urls.txt, initialize total number of images downloaded
rows = open(args["urls"]).read().strip().split("\n")
total = 0

for url in rows:
	try:
		r = requests.get(url, timeout=60)

		p = os.path.sep.join([args["output"], "{}.jpg".format(
			str(total).zfill(8))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()
    
		print("[INFO] downloaded: {}".format(p))
		total += 1

	# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading {}...skipping".format(p))


for imagePath in paths.list_images(args["output"]):
	delete = False

	try:
		image = cv2.imread(imagePath)

		if image is None:
			print("None")
			delete = True

	except:
		print("Except")
		delete = True

	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)
