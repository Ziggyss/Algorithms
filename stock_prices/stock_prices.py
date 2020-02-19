#!/usr/bin/python

import argparse

# test = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
  for i in range (0, len(prices)):
    max_value = max(prices)
    max_index = prices.index(max_value)
    if max_index > 0:
        min_value = min(prices[0:max_index]) 
        result = max_value - min_value
    else:
      result = prices[1] - prices[0]    
    return result   

# This is my first pass solution, but it doesn't work for the fourth test. I misunderstood what needed to be done with edge cases where the max value is at the beginning of the array. Now working on a better solution.
  
# print(find_max_profit(test))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))