"""
辅助函数
"""

import matplotlib.pyplot as plt
import scipy.io as sio
import os


def save_matrix(matrix, file_name):
    """保存指定布局矩阵
            Args:
                matrix(ndarray): 布局板矩阵
                file_name (str): 矩阵文件名
    """
    sio.savemat(file_name+".mat", {'matrix': matrix})


def save_fig(matrix, file_name):
    """保存图片

            Args:
                matrix(ndarray): 布局板矩阵 \n
                file_name (str): 图片文件名 \n
    """
    plt.imshow(matrix)
    plt.savefig(file_name+".jpg")


def make_dir(outdir):
    """建立文件夹

            Args:
                outdir(str): 生成的矩阵和图片文件的保存路径 \n
    """
    if not os.path.exists(outdir):
        os.makedirs(outdir)
