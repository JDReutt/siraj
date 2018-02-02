import numpy as numpy
from functools import partial
import PIL.Image
import tensorflow as tf
import urllib.request
import os
import zipfile

def main():
	#Step 1 - download pretrained neural network
	url = 'https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip'
	model_name = os.path.split(url)[-1]
	local_zip_file = os.path.join(data_dir, model_name)
	if not os.path.exists(local_zip_file):
		#download
		model_url = urllib
