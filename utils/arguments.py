import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--model",
                        default="gpt-2-small",
                        choices=["gpt-3-small", "BERT"],
                        help="Select language model to use")
    parser.add_argument("--debug",
                        default=False,
                        action="store_true",
                        help="Run server in debug mode")
    parser.add_argument("--address",
                        default="127.0.0.1",
                        help="Address to bind server to (0.0.0.0 for nonlocal use)")
    parser.add_argument("--port",
                        default="5000",
                        help="Port to launch UI and API (default:5001)")
    parser.add_argument("--nocache",
                        default=False,
                        action="store_true",
                        help="Disable caching")
    parser.add_argument("--dir",
                        type=str,
                        default=os.path.abspath("../data"),
                        help="Directory to scan for ???")
    parser.add_argument("--no_cors",
                        action="store_true",
                        help="Launch API without CORS support")

    return parser.parse_args()

