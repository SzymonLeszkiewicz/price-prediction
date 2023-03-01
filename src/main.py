#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import argparse
import textwrap

from const import help_description, mode_help_description, epilog_text, city_help_description, cities


class Main:
    def __init__(self):
        self.mode = None

    def run(self):
        parser = argparse.ArgumentParser(description=help_description, epilog=epilog_text, prog='PRICE PREDICTION',
                                         formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('mode', metavar='mode', type=str, help=mode_help_description, choices=['i', 'm', 'e'])
        parser.add_argument('-city', metavar='city', type=str, help=textwrap.fill(city_help_description),
                            choices=cities)

        args = parser.parse_args()
        self.mode = args.mode
        self.city = args.city

    def check_arguments(self):
        pass

    def run_best_city_to_invest(self):
        pass

    def run_best_city_to_monetize_investment(self):
        pass

    def run_evaluate_market(self):
        pass

    def run_predict_house_price(self):
        pass


if __name__ == '__main__':
    main = Main()
    main.run()
    if main.mode == 'i':
        main.run_best_city_to_invest()

    elif main.mode == 'm':
        main.run_best_city_to_monetize_investment()
    else:
        main.run_evaluate_market()
