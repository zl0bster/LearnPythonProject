
import sys
import argparse
r"""
sample arguments:
python print_args.py  -x 1202 -y 803  r -nba 20 -nbr 3
python print_args.py  -x 1202 -y 803  d -file C:\Users\1\PycharmProjects\LearnPythonProject\test.txt
python print_args.py  -x 1202 -y 803  d -file test.txt
"""


def main():
    parser = parserDefinition()
    args = parser.parse_args()

    print(sys.argv[0])
    print(sys.argv[1:])
    print('*' * 12)
    print(args)
    # print(args.m)
    print(args.xres)
    print(args.yres)
    if args.mode == 'r':
        print(args.nba, args.nbr)
    if args.mode == 'd':
        print(str(args.file))


def parserDefinition():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xres', help='window x resolution', type=int, default=1200)
    parser.add_argument('-y', '--yres', help='window y resolution', type=int, default=800)
    subparsers = parser.add_subparsers(dest='mode')
    randParser = subparsers.add_parser('r')
    randParser.add_argument('-nba', help='number of balls', type=int, required=True)
    randParser.add_argument('-nbr', help='number of bricks', type=int, required=True)
    defParser = subparsers.add_parser('d')
    defParser.add_argument('-file', type=argparse.FileType('r'), help='scene config file path', required=True)

    # parser.add_argument('-nba', help='number of balls', type=int)
    # parser.add_argument('-nbr', help='number of bricks', type=int)
    # parser.add_argument('-m', "--mode", type=str, choices=['R', 'D'], help='r for random, d for predefined')

    return parser


if __name__ == '__main__':
    main()
