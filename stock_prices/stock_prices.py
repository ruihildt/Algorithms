#!/usr/bin/python

import argparse

def find_max_profit(prices):
  possible_wins=[]
  # loop through all resale prices
  for i in range(len(prices)-1):
    # make a list of possible resale price for a day
    resale_prices = prices[i+1:]
    # calculate the amount you can get for each subsequent day
    for resale_p in resale_prices:
      diff = resale_p - prices[i]
      possible_wins.append(diff)

  # find the max of all values
  max_profit = max(possible_wins)

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))