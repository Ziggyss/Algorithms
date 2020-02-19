#!/usr/bin/python

import argparse


def find_max_profit(prices):
    differences = [0] * (len(prices)-1)
    for i in range (1, len(prices)):
      lowest_price = min(prices[0:i])
      lowest_index = prices.index(lowest_price)
      current_price = prices[i]
      profit = current_price - lowest_price 
      differences[i-1] = profit
    return max(differences)   



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))