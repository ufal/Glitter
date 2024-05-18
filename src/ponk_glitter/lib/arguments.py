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

