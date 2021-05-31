import csv
import sys

path_to_file = './Resources/election_data.csv'
path_to_output_file = './Resources/output.txt'

with open(path_to_file, newline='') as f:
    # row count
    # starts in -1 to exclude the header row from the record count
    row_count = -1

    # voter has vote
    has_voted = {}
    # total votes
    total_votes = 0
    # candidate votes
    candidate_votes = {}

    # initialize csv reader
    reader = csv.reader(f)

    # go through each row
    for [voter_id, county, candidate] in reader:

        # case is a record
        if row_count >= 0:

            # check if voter has vote
            if voter_id in has_voted:
                print('Voter already voted. Ignore...')
                continue
            
            has_voted[voter_id] = True

            # increase total votes
            total_votes = total_votes + 1

            # totalize for current candidate
            if candidate in candidate_votes:
                candidate_votes[candidate] = candidate_votes[candidate] + 1
            else:
                candidate_votes[candidate] = 1

        # increment record count
        row_count = row_count + 1

to_file = []
print('Election Results')
to_file.append('Election Results\n')
print('-------------------------')
to_file.append('-------------------------\n')
print(f'Total Votes: {total_votes}')
to_file.append(f'Total Votes: {total_votes}\n')
print('-------------------------')
to_file.append('-------------------------\n')
winner = ('', sys.maxsize * -1)
for candidate, votes in candidate_votes.items():
    print(f'{candidate}: {votes/total_votes * 100}% ({votes})')
    to_file.append(f'{candidate}: {votes/total_votes * 100}% ({votes})\n')
    if votes > winner[1]:
        winner = (candidate, votes)
print('-------------------------')
to_file.append('-------------------------\n')
print(f'Winner: {winner[0]}')
to_file.append(f'Winner: {winner[0]}\n')
print('-------------------------')
to_file.append('-------------------------\n')

# write to file
output_file = open(path_to_output_file, 'w')
output_file.writelines(to_file)
output_file.close()
