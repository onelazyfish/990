# TODO 正确导入函数 generate_matrix, save_matrix, save_fig

from cli import get_options  # TODO: 保证不修改本行也可以正确导入
from generator.core import generate_matrix
from generator.utils import save_matrix, save_fig, make_dir


def main():
    """主函数将调用自定义的get_options()，generate_matrix，make_dir， save_matrix，save_fig等函数
    """
    # TODO 使用导入的函数按命令行参数生成数据，包括 mat 文件与 jpg 文件
    op = get_options()
    mat = generate_matrix(op.board_grid, op.unit_grid,
                          op.unit_n, op.positions)
    make_dir(op.outdir)
    path = op.outdir + '/' + op.file_name
    save_matrix(mat, path)
    save_fig(mat, path)


if __name__ == "__main__":
    main()
