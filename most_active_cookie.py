import argparse
import cookie_utilities

parser = argparse.ArgumentParser()
parser.add_argument('csv_path', type = str)
parser.add_argument('-d', type = str)
args = parser.parse_args()

csv = open(args.csv_path)
cookie_per_day = cookie_utilities.cookies_per_day(csv)

for cookie in cookie_utilities.most_frequent_cookies(args.d, cookie_per_day):
    print(cookie)
