#!/usr/bin/python

import argparse


def find_max_profit(prices):
    differences = [0] * (len(prices)-1) #O(1)
    for i in range (1, len(prices)):    #O(n)
      lowest_price = min(prices[0:i])   #Is this also O(n) because of min?
      lowest_index = prices.index(lowest_price) #O(1)
      current_price = prices[i]                #O(1)
      profit = current_price - lowest_price    #O(1)
      differences[i-1] = profit                #O(1)
    return max(differences)                    #O(n) because of max?

# The complexity of the code I've written would be O(n ^ 2)   



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))