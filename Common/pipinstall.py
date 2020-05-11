#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @aluer : tangmy
# @createtime: 20200511


import os
import random


# 需要安装的第三方库
libs = {"requests", "requests_toolbelt"}

# 国内镜像源
mirror_1 = "http://mirrors.aliyun.com/pypi/simple/"  # 阿里云
mirror_2 = "https://pypi.mirrors.ustc.edu.cn/simple/"  # 中国科技大学
mirror_3 = "http://pypi.douban.com/simple/"  # 豆瓣(douban)
mirror_4 = "https://pypi.tuna.tsinghua.edu.cn/simple/"  # 清华大学
mirror_5 = "http://pypi.mirrors.ustc.edu.cn/simple/"  # 中国科学技术大学
mirror_list = [mirror_1, mirror_2, mirror_3, mirror_4, mirror_5]



def pip_install(temp_mirror):
	"""
	pip 安装所需库
	Returns:无

	"""
	try:
		failed_list = []
		# log.info("Use Mirror: " + temp_mirror)
		for lib in libs:
			# log.info(f"Strat to install: {lib}")
			res = os.system(f"pip3 install {lib} -i {temp_mirror}")
			if res == 1:
				failed_list.append(lib)
	except Exception as e:
		print(e)
	# finally:
	# 	if failed_list:
	# 		# log.error(f"pip3 install failed list :{failed_list}!")
	# 	else:
	# 		# log.info(f"pip3 install all sucess!")
    #

if __name__ == '__main__':
	temp_mirror = random.choice(mirror_list)
	pip_install(temp_mirror)
