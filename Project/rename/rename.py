#coding:utf-8
import os
path = './'
def main():
	for foldername in os.listdir(path):
		if os.path.isdir(foldername):
			filepath = (path + '/' + foldername)
			for parent, dirnames, filenames in os.walk(filepath):
				num = 0
				for filename in filenames:
					num = num + 1
					if os.path.isfile(filepath + '/' + filename):
						re_name(foldername, filename, num)
	print('success')

def re_name(foldername, filename, num):
	new_name = foldername + str(num)
	old_file = foldername + '/' + filename
	new_flie = foldername + '/MaskImages/'+ new_name + '.jpg'
	os.rename(old_file, new_flie)

main()
