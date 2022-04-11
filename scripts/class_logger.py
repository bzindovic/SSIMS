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

from time import time


def time_hms(time: float) -> tuple:
	hours = int(time // 3600)
	minutes = int((time - hours * 3600) // 60)
	seconds = int(time % 60)

	return hours, minutes, seconds


class Logger:
	"""
	Simple class for .txt logging.
	Initialize with path to .txt log file.
	Use .log(str) to write to file.
	Use .close() to close the file.
	"""

	def __init__(self, path: str):
		self.file = open(path, 'w')

	def log(self, string: str, to_print=False) -> bool:
		try:
			h, m, s = time_hms(time())
			h = str(h + 2).rjust(2, '0')
			m = str(m).rjust(2, '0')
			s = str(s).rjust(2, '0')
			self.file.write('{}:{}:{} -> {}\n'.format(h, m, s, string))

			if to_print:
				print(string)

			return True

		except IOError:
			return False

	def close(self):
		self.file.close()