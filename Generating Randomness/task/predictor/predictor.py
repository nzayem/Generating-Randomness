number_length = 100
patterns = ['000', '001', '010', '011', '100', '101', '110', '111']
target_number = []
text = ''
freq_dict = dict.fromkeys(patterns, [])
pattern_freq = dict.fromkeys(patterns, 0)  # Stage 3: Count frequency of each pattern
first_triad = ''
balance = 1000  # Stage 4

print("Please give AI some data to learn..."
      "\nThe current data length is 0, 100 symbols left")

# Start of the Filter code
while True:
    user_input = input('Print a random string containing 0 or 1:\n\n')
    filtered_symbols = [x for x in user_input if x == '0' or x == '1']
    target_number.extend(filtered_symbols)

    if len(target_number) >= number_length:
        break
    else:
        print(f'Current data length is {len(target_number)}, {number_length - len(target_number)} symbols left')

print('\nFinal data string:')

for digit in target_number:
    text += digit

print(f'{text}\n')
# End of the filter code

# Start of the patterns Frequency calculator

for pattern in patterns:

    try:
        full_text_list = [text[i + 3] for i in range(len(text)) if text.startswith(pattern, i)]

        freq_dict[pattern] = [full_text_list.count('0'), full_text_list.count('1')]
        # calculating the frequency of each pattern to select which one to start with
        pattern_freq[pattern] = text.count(pattern)

    except IndexError:

        truncated_text_list = [text[i + 3] for i in range(len(text) - 3) if text.startswith(pattern, i)]

        freq_dict[pattern] = [truncated_text_list.count('0'), truncated_text_list.count('1')]

# for key, value in freq_dict.items():
#
#     print(f'{key}: {value[0]},{value[1]}')
# End of the patterns Frequency calculator

# Stage 3:
# To predict the first triad, although it's enough for this stage to choose that randomly
# we can check the frequency of the triad during all inputs, and pick the highest freq.

# Getting the pattern with the highest frequency and setting the first triad:

triad_frequency_sorted = sorted(pattern_freq.values())

for key, value in pattern_freq.items():
    if value == triad_frequency_sorted[-1]:
        first_triad += key

# for the 3rd case where count of 0 == count of 1, will pick the most frequent digit in the Final Data String

most_frequent = '0' if text.count('0') >= text.count('1') else '1'

print("You have $1000. Every time the system successfully predicts your next press, you lose $1."
      "\nOtherwise, you earn $1. Print 'enough' to leave the game. Let's go!")


def prediction_accuracy(estimation, data):
    counter = 0
    for x in range(len(estimation) - 3):
        if estimation[3:][x] == data[3:][x]:
            counter += 1
    return counter


while True:
    try:
        user_test = input("\nPrint a random string containing 0 or 1:\n")

        if user_test == 'enough':
            print('Game over!')
            break

        else:

            prediction = first_triad

            for i in range(len(user_test) - 3):

                combination = user_test[i:i+3]

                if freq_dict[combination][0] > freq_dict[combination][1]:
                    prediction += '0'

                elif freq_dict[combination][0] < freq_dict[combination][1]:
                    prediction += '1'

                else:
                    prediction += most_frequent

            print("prediction:")
            print(prediction)

            accuracy = prediction_accuracy(prediction, user_test)

            balance = balance - accuracy + len(user_test) - accuracy - 3

            print("Computer guessed right {} out of {} symbols ({:03.2f} %)"
                  .format(accuracy, len(user_test) - 3, 100 * accuracy / (len(user_test) - 3)))

            print(f"Your balance is now ${balance}")

    except KeyError:
        continue
