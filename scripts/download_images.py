# USAGE example:
# python download_images.py --urls urls.txt --output images/face --name face

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
ap.add_argument("-n", "--name", required=True,
	help="file name")
args = vars(ap.parse_args())

rows = open(args["urls"]).read().strip().split("\n")
name = args["name"]
total = 0

for url in rows:
	try:

		r = requests.get(url, timeout=60)

		p = os.path.sep.join([args["output"], "{}.jpg".format(str(name) + str(total).zfill(4))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		print("[INFO] downloaded: {}".format(p))
		total += 1

	except:
		print("[INFO] error downloading {}...skipping".format(p))

for imagePath in paths.list_images(args["output"]):
	delete = False

	try:
		image = cv2.imread(imagePath)

		# if the image is `None` then we could not properly load it
		# from disk, so delete it
		if image is None:
			print("None")
			delete = True

	# if OpenCV cannot load the image then the image is likely
	# corrupt so we should delete it
	except:
		print("Except")
		delete = True

	# check to see if the image should be deleted
	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)
