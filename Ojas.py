import sys

file_name = sys.argv[-1]
file = open(file_name)
all_words = list(file.read().split())

for i in range(0, len(all_words) // 2):
    word1 = all_words[2*i]
    word2 = all_words[2*i+1]

    linear_d = 0
    circular_d = 0


    for i in range(len(word1)):

        value_1 = ord(word1[i]) - 96
        value_2 = ord(word2[i]) - 96

        linear_d += abs(value_1 - value_2)
        circular_d += min(abs(value_1 - value_2) , 26 - max(value_1, value_2) + min(value_1, value_2))

    print(linear_d, circular_d)