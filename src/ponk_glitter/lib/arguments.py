import argparse
import os


def get_server_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug",
                        default=False,
                        action="store_true",
                        help="Run server in debug mode")
    parser.add_argument("--host",
                        default="127.0.0.1",
                        help="Address to bind server to (0.0.0.0 for nonlocal use)")
    parser.add_argument("--port",
                        default="4000",
                        help="Port to launch UI and API (default:5001)")
    return parser.parse_args()


def get_cli_args():
    parser = argparse.ArgumentParser()

    export_options = parser.add_mutually_exclusive_group()
    export_options.add_argument("--to-json",
                                default=False,
                                action="store_true",
                                help="export data to JSON")
    export_options.add_argument("--to-html",
                                default=False,
                                action="store_true",
                                help="export data to HTML")
    export_options.add_argument("--to-dict",
                                default=False,
                                action="store_true",
                                help="export data to python dictionary")
    export_options.add_argument("--to-table",
                                default=False,
                                action="store_true",
                                help="export data to table")

    parser.add_argument("--output",
                        default="/dev/stdout",
                        help="output file name (default: stdout)")
    parser.add_argument("--input",
                        default="/dev/stdin",
                        help="input file name (default: stdin)")
    parser.add_argument("--model",
                        default="Robeczech",
                        help="name of model you want to use to glitter text (default: Robeczech)")

    return parser.parse_args()

