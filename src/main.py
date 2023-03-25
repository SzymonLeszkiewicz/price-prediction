#  Copyright (c)
#  Author: Szymon Leszkiewicz
#  Date: 2023 - 2
#  License: BSD 3-Clause
#  Description: This file is part of the project: "House prices prediction in Poland based on the
#               migration data and the real estate market data".
import argparse
import textwrap
from run_pred import Predict
from const import Const

c = Const()


class Main:
    def __init__(self):
        self.mode = None
        self.city = None
        self.prediction = Predict().prediction
    def run(self):
        parser = argparse.ArgumentParser(description=c.help_description, epilog=c.epilog_text, prog='PRICE PREDICTION',
                                         formatter_class=argparse.RawTextHelpFormatter)
        parser.add_argument('mode', metavar='mode', type=str, help=c.mode_help_description, choices=['i', 'm', 'e'])
        parser.add_argument('-city', metavar='city', type=str, help=textwrap.fill(c.city_help_description),
                            choices=c.cities)

        args = parser.parse_args()
        self.mode = args.mode
        self.city = args.city

    def check_arguments(self):
        pass

    def run_best_city_to_invest(self):
        pass

    def run_best_city_to_monetize_investment(self):
        print(max(self.prediction))
        

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
