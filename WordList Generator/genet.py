import argparse
import itertools
import os


def generator(input_path, output_path):
    # read the lines from the input file and split them into words
    words = []
    with open(input_path, 'r') as f:
        for line in f:
            words += line.strip().split()

   
    passwords = []
    for i in range(1, len(words) + 1):
        for combination in itertools.combinations(words, i):
            passwords.append(''.join(combination))
        for permutation in itertools.permutations(words, i):
            passwords.append(''.join(permutation))

    # write the password candidates to text file
    with open(output_path, 'w') as f:
        for password in passwords:
            f.write(password + '\n')

    print(f'Password candidates written to {output_path}')


def main():
    # defining command-line arguments and options using argparse

    parser = argparse.ArgumentParser(description='Generate password candidates from a text file of words or phrases')
    parser.add_argument('input_file', metavar='input_file', type=str, help='path to input text file')
    parser.add_argument('-o', dest='output_file', type=str, default='passwords.txt',
                        help='path to output file (default: passwords.txt)')

    # command-line arguments
    args = parser.parse_args()

    # Check if the input file exists if not print Error
    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} not found')
        exit()

    # Generate passwords and write them to the output text file 
    generator(args.input_file, args.output_file)


if __name__ == '__main__':
    main()
