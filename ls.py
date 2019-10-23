#!/usr/bin/python3

import argparse



class ls(object):

    
    def __init__(self):
        parser = argparse.ArgumentParser(description='Linux Command Python: ls.')

        # 可选参数，格式参数
        parser.add_argument('-a', '--all', help='show allf files', action='store_true', required=False)
        parser.add_argument('-l', '--long', help='view long files', action='store_true', required=False)


        # 位置参数
        parser.add_argument("path", type=str, help="The path", nargs="?")
        args = parser.parse_args()
        print(args)
        print(vars(args))

    def run(self):
        print("Linux Command: ls")

        


if __name__ == "__main__":
    ls = ls()


    ls.run()