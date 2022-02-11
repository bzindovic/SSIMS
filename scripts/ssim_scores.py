#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This package is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this package. If not, you can get eh GNU GPL from
https://www.gnu.org/licenses/gpl-3.0.en.html.

Created by Robert Ljubicic.
"""

try:
	from __init__ import *
	from os import path, listdir
	from glob import glob
	from math import log

	import matplotlib.pyplot as plt

except Exception as ex:
	print('\n[EXCEPTION] Import failed: \n\n'
		  '  {}'.format(ex))
	input('\nPress ENTER/RETURN to exit...')
	exit()


def keypress(event):
	if event.key == 'escape':
		plt.close()


try:
	parser = ArgumentParser()
	parser.add_argument('--folder', type=str, help='Path to stabilization folder')
	args = parser.parse_args()

	fold = args.folder
	ssim_path = r'{}/ssim_scores.txt'.format(fold)

	if not path.exists(ssim_path):
		print('[ERROR] SSIM scores file not found in folder [{}]!'.format(fold))
		exit()

	data = np.loadtxt(ssim_path, dtype='float')
	num_markers = data.shape[1]
	marker_indices = list(range(1, num_markers + 1))

	fig, ax = plt.subplots()
	fig.canvas.mpl_connect('key_press_event', keypress)

	plt.boxplot(data)
	xlim = plt.xlim()
	plt.plot(xlim, [1, 1], 'k--')
	plt.xlim(xlim)
	plt.xticks(marker_indices)
	plt.xlabel('Feature # [-]')
	plt.ylabel('SSIM score [-]')
	plt.title('Higher score is better, perfect score = 1')

	try:
		mng = plt.get_current_fig_manager()
		mng.window.state('zoomed')
		mng.set_window_title('SSIM score comparison')
	except:
		pass

	plt.show()

except Exception as ex:
	print('\n[EXCEPTION] The following exception has occurred: \n\n'
		  '  {}'.format(ex))
	input('\nPress ENTER/RETURN to exit...')