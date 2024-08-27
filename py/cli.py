import argparse

parser = argparse.ArgumentParser(description="Titanic项目的cli工具",)
parser.add_argument("-m", "--mode", type=str, default="train", help="运行模式，train表示训练，predict表示预测")
parser.print_help()