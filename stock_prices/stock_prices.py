#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # loop through all resale prices
  for i in range(len(prices)-1):
    # make a list of possible resale price for an initial day
    resale_prices = prices[i+1:]
    # calculate the amount you can get for each subsequent day
    for resale_p in resale_prices:
      diff = resale_p - prices[i]
      if i == 0:
        max_profit = diff
        min_profit = diff
        break
      if diff >= max_profit:
        max_profit = diff
      elif diff <= min_profit:
        min_profit = diff
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))