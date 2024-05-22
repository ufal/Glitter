#!/usr/bin/env python3
from models.robeczech import Robeczech
from lib.tui import print_glittered_text, print_table_of_glittered_text
from lib.arguments import get_cli_args


RBCZ = Robeczech()


if __name__ == '__main__':
    args = get_cli_args()
    input_file = args.input if args.input else "/dev/stdin"
    output_file = args.output if args.output else "/dev/stdout"

    with open(input_file, "r") as file:
        text = file.read()
        gt = RBCZ.glitter_text(text)

    if args.to_json:
        with open(output_file, "w") as file:
            file.write(gt.to_json())
    elif args.to_html:
        with open(output_file, "w") as file:
            file.write(gt.to_html())
    elif args.to_dict:
        with open(output_file, "w") as file:
            file.write(str(gt.to_dict()))
    else:
        print_table_of_glittered_text(gt)
        print("\n")
        print_glittered_text(gt)
