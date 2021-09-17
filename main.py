from src.views.web.start import app
from src.views.console.view_menu import ViewMenu
import argparse

class Main:

    @staticmethod
    def define_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--cli', dest='cli', action='store_true', help='To run the application in terminal view')
        return parser

    @staticmethod
    def run_cli():
        console = ViewMenu()
        console.execute()

    @staticmethod
    def run_web():
        app.run(debug=True)

if __name__ == '__main__':
    parser = Main.define_args()
    args = parser.parse_args()

    if args.cli:
        Main.run_cli()
    else:
        Main.run_web()