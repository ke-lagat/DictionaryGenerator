import re
import os
import sys
import tqdm

leet_map = {
    'a': ['@', '4', '^', '/\\', 'æ'],
    'b': ['8', 'ß', '13', '|3'],
    'c': ['(', '<', '{', '[', '¢'],
    'd': ['|)', 'cl', 'đ'],
    'e': ['3', '€', 'ë'],
    'f': ['|=', 'ph'],
    'g': ['6', '9', '&'],
    'h': ['#', '|-|', '[-]'],
    'i': ['1', '!', '|', '¡'],
    'j': ['_|', '_/'],
    'k': ['|<', '|{'],
    'l': ['1', '|', '£', '¬'],
    'm': ['^^', '/\\/\\', '(V)', '(u)'],
    'n': ['^/', '|\\|', '/\\/', 'И'],
    'o': ['0', '()', '*'],
    'p': ['|*', '|o', '|º', '¶'],
    'q': ['(,)', '0_', 'kw'],
    'r': ['|2', '12', '.-', 'Я'],
    's': ['$', '5', '§'],
    't': ['7', '+', '†'],
    'u': ['|_|', 'µ', '[_]'],
    'v': ['\\/', '|/', '\\|'],
    'w': ['\\/\\/', 'vv', '\\^/', '`//'],
    'x': ['%', '><', '}{'],
    'y': ['`/', '¥', 'j'],
    'z': ['2', '≥', '7_']
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("="*60)
    print("   DICTIONARY GENERATOR")
    print("="*60)

def generate_leet_variations(word, max_variations=10000):
    variations = ['']
    for char in word.lower():
        new_variations = []
        substitutions = leet_map.get(char, []) + [char]
        for variant in variations:
            for sub in substitutions:
                new_variations.append(variant + sub)
                if len(new_variations) > max_variations:
                    return new_variations
        variations = new_variations
    return variations

def insert_number(base, number):
    num_str = str(number)
    return [base[:i] + num_str + base[i:] for i in range(len(base) + 1)]

def add_symbol_variations(base, symbols):
    variations = []
    for s in symbols:
        variations.append(s + base)
        variations.append(base + s)
    for s in symbols:
        if re.match(r'^\d+[a-zA-Z]+$', base):
            split_idx = re.search(r'\d(?=\D)', base).end()
            variations.append(base[:split_idx] + s + base[split_idx:])
        elif re.match(r'^[a-zA-Z]+\d+$', base):
            split_idx = re.search(r'\D(?=\d)', base).end()
            variations.append(base[:split_idx] + s + base[split_idx:])
    return variations

def generate_combinations(words, numbers, symbols, max_variations=10000):
    combinations_set = set()

    for word in tqdm.tqdm(words, desc="Generating variations"):
        for word_case in [word.lower(), word.upper(), word.capitalize()]:
            leet_words = generate_leet_variations(word_case, max_variations)
            for lw in leet_words:
                combinations_set.add(lw)
                for num in numbers:
                    prepend = str(num) + lw
                    combinations_set.update(add_symbol_variations(prepend, symbols))
                    append = lw + str(num)
                    combinations_set.update(add_symbol_variations(append, symbols))
                    for inserted in insert_number(lw, num):
                        combinations_set.add(inserted)
                        combinations_set.update(add_symbol_variations(inserted, symbols))
    return combinations_set


def interactive_mode():
    words = input("Enter words (comma-separated): ").strip().split(',')
    numbers = input("Enter numbers (comma-separated): ").strip().split(',')
    output_file = input("Enter output file name (default: password_dictionary.txt): ").strip()
    max_var_input = input("Enter maximum leet variations per word (default: 10000): ").strip()

    if not output_file:
        output_file = "password_dictionary.txt"
    max_variations = int(max_var_input) if max_var_input.isdigit() else 10000

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '=', '?']

    dictionary = generate_combinations([w.strip() for w in words], [n.strip() for n in numbers], symbols, max_variations=max_variations)

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in sorted(dictionary):
            f.write(f"{item}\n")

    print(f"\nGenerated {len(dictionary)} combinations and saved to {output_file}")

def main():
    clear_terminal()
    banner()
    print("Interactive mode selected.")
    interactive_mode()

if __name__ == "__main__":
    main()
