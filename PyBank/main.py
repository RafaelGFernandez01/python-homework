import csv
import sys

path_to_file = './Resources/budget_data.csv'
path_to_output_file = './Resources/output.txt'

with open(path_to_file, newline='') as f:
    # profit/loss by months
    profit_loss_by_months = {}

    # total profit
    total_profit = 0

    # previous profit
    previous_profit = 0
    changes = 0
    max_change = ('', sys.maxsize * -1)
    min_change = ('', sys.maxsize)

    # row count
    # starts in -1 to exclude the header row from the record count
    row_count = -1

    # initialize csv reader
    reader = csv.reader(f)

    # go through each row
    for [month, profit] in reader:

        # case is a record
        if row_count >= 0:
            
            # add profit/loss record
            profit_loss_by_months[month] = float(profit)

            # acum profit for total
            total_profit = total_profit + float(profit)

            # change
            change = float(profit) - previous_profit
            previous_profit = float(profit)

            # add change to get average
            if row_count > 0:
                changes = changes + change

            # check for a new max
            if (change > max_change[1]):
                max_change = (month, change)

            # check for a new min
            if (change < min_change[1]):
                min_change = (month, change)

        # increment record count
        row_count = row_count + 1

# print results to console
print('Financial Analysis')
print(' ----------------------------')
print(f' Total Months: {len(profit_loss_by_months)}')
print(f' Total: ${total_profit}')
print(f' Average  Change: ${changes/len(profit_loss_by_months) - 1}')
print(f' Greatest Increase in Profits: {max_change[0]} (${max_change[1]})')
print(f' Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})')

# write to file
output_file = open(path_to_output_file, 'w')
output_file.write('Financial Analysis\n')
output_file.write(' ----------------------------\n')
output_file.write(f' Total Months: {len(profit_loss_by_months)}\n')
output_file.write(f' Total: ${total_profit}\n')
output_file.write(f' Average  Change: ${changes/len(profit_loss_by_months) - 1}\n')
output_file.write(f' Greatest Increase in Profits: {max_change[0]} (${max_change[1]})\n')
output_file.write(f' Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})\n')
output_file.close()
