#!/usr/bin/env python3

# 0.51 per hour
costPerHour = 0.51

# costs for one server
dayCost = costPerHour * 24
monthCost = dayCost * 31

print('Cost to operate one server per day is ${:.2f}.'.format(dayCost))
print('Cost to operate one server per month is ${:.2f}.'.format(monthCost))

savings = 918
budgetDays = savings / dayCost

twentyServersDayCost = 20 * dayCost
twentyServersMonthCost = 20 * monthCost

print('Cost to operate twenty servers per day is ${:.2f}.'.format(twentyServersDayCost))
print('Cost to operate twenty servers per month is ${:.2f}.'.format(twentyServersMonthCost))
print('A server can operate on a ${0:.2f} budget for {1:.0f} days.'.format(savings, budgetDays))