# https://github.com/qq456cvb/SfM/blob/23d36d70591ce024483c4136fd718421c4b129df/SFM/utils.py
# https://github.com/akshitj1/dtam/blob/bd027b6f76215cc71af382f5e7015f11a726cace/mapper.cpp
import os

	
def write_imgf_R_t(txtdir = 'fountain-P11/gt_dense_cameras/', imgdir = 'fountain-P11/images/', dst = "p11_tf.txt"):
	with open(dst, 'w') as f:
		f.write("SfM_quality_evaluation, fountain-P11\ntimestamp R(rotation) t(translation)\n")
		for i in range(11):
			src = txtdir + '00{:02d}.jpg.camera'.format(i)
			if not os.path.isfile(src):
				raise FileNotFoundError(src)
			imgfilename = src[-15:-7]
			# print(imgfilename)
			if not os.path.isdir(imgdir):
				raise NotADirectoryError(imgdir)
			if not os.path.isfile(imgdir + imgfilename):
				raise FileNotFoundError(imgdir + imgfilename)
			# print(imgdir + imgfilename)
			lines = open(src).readlines()
			
			# f.write(imgdir + imgfilename)
			f.write(src[-15:-11])
			f.write("\t")
			for line in lines[4:7]:
				R =line.split()
				f.write(f'{R[0]}\t{R[1]}\t{R[2]}\t')
			t = lines[7].split()
			f.write(f'{t[0]}\t{t[1]}\t{t[2]}\n')
			
				
			
	# lines = open(src).readlines()
	# print(lines[4:8])

	# print([[s for s in line.split()] for line in lines[4:8]])
	# R00, R01, R02, R10, R11, R12, R20, R21, R22, tx, ty, tz = 
	# with open(dst_file, 'w') as f:
	#     for line in lines[4:8]:
	#         s =line.split()
	#         f.write(f'{s[0]} {s[1]}')
		


if __name__ == '__main__':
	txtdir = 'fountain-P11/gt_dense_cameras/'
	imgdir = 'fountain-P11/images/'
	dst = "p11_tf.txt"
	# write_imgf_R_t('fountain-P11/gt_dense_cameras/00{:02d}.jpg.camera'.format(0), imgdir, dst_file)
	# for i in range(11):
		# write_imgf_R_t('fountain-P11/gt_dense_cameras/00{:02d}.jpg.camera'.format(i))
	write_imgf_R_t(txtdir, imgdir, dst)