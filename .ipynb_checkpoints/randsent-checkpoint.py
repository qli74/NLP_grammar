#!/usr/bin/env python
"""
601.465/665 — Natural Language Processing
Assignment 1: Designing Context-Free Grammars

Assignment written by Jason Eisner
Modified by Kevin Duh
Re-modified by Alexandra DeLucia

Code template written by Alexandra DeLucia,
based on the submitted assignment with Keith Harrigian
and Carlos Aguirre Fall 2019
"""
import os
import sys
import random
import argparse

# Want to know what command-line arguments a program allows?
# Commonly you can ask by passing it the --help option, like this:
#     python randsent.py --help
# This is possible for any program that processes its command-line
# arguments using the argparse module, as we do below.
# 
# NOTE: Parsing the command-line arguments is NOT the same as parsing
# a natural-language sentence! But in both cases, "parsing" a string
# means identifying the elements of the string and the roles they play.

def parse_args():
    """
    Parse command-line arguments.

    Returns:
        args (an argparse.Namespace): Stores command-line attributes
    """
    # Initialize parser
    parser = argparse.ArgumentParser(description="Generate random sentences from a PCFG")
    # Grammar file argument (required)
    parser.add_argument(
        "-g",
        "--grammar-file", 
        type=str, required=True, 
        help="Path to grammar file",
    )
    # Number of sentences
    parser.add_argument(
        "-n",
        "--number-of-sentences",
        type=int,
        help="Number of sentences to generate.",
        default=1,
    )
    # Maximum number of nonterminal expansions when generating the sentence (see question 2(f))
    parser.add_argument(
        "-M",
        "--max-expansions",
        type=int,
        help="Max number of non-terminal expansions to follow for sentence generation",
        default=450,
    )
    # Print the derivation tree for each sentence
    parser.add_argument(
        "-t",
        "--tree",
        action="store_true",
        help="Print the derivation tree for each generated sentence",
        default=False,
    )
    return parser.parse_args()


class Grammar:
    def __init__(self, grammar_file):
        """
        Context-Free Grammar (CFG) Sentence Generator

        Args:
            grammar_file (str): Path to a .gr grammar file
        
        Returns:
            self
        """
        # Parse the input grammar file
        self.rules = None
        self._load_rules_from_file(grammar_file)

    def _load_rules_from_file(self, grammar_file):
        """
        Read grammar file and store its rules in self.rules

        Args:
            grammar_file (str): Path to the raw grammar file 
        """
        rules={}
        with open(grammar_file,'r') as f:
            lines=f.readlines()
        for line in lines:
            if line[0] not in ['#','\n']:
                line=line.strip('\n').replace('    ','\t').split('\t')
                weights=float(line[0])
                symbols=line[2].split(' ')
                if line[1] not in rules.keys():
                    rules[line[1]]={'weights':[weights],'symbols':[symbols]}
                else:
                    rules[line[1]]['weights'].append(weights)
                    rules[line[1]]['symbols'].append(symbols)
        self.rules=rules

    def sample(self, current, derivation_tree, max_expansions):
        """
        Sample a random sentence from this grammar

        Args:
            derivation_tree (bool): if true, the returned string will represent 
                the tree (using bracket notation) that records how the sentence 
                was derived
                               
            max_expansions (int): max number of nonterminal expansions we allow
        
        Returns:
            str: the random sentence or its derivation tree
        """

        # Check number of expansions (<=max_expansions)
        if current=='ROOT':
            self.count = 0
        else:
            if self.count>max_expansions:
                return '...'

        rules=self.rules[current]
        # Randomly select one rule
        picked_rule=random.choices(rules['symbols'], weights=rules['weights'],k=1)[0]

        if derivation_tree:
            result=[current]
        else:
            result = []

        for i in range(len(picked_rule)):
            if picked_rule[i] in self.rules.keys():
                self.count += 1
                result.append(self.sample(picked_rule[i], derivation_tree, max_expansions))
            else:
                result.append(picked_rule[i])

        return result

####################
### Main Program
####################
def main():
    # Parse command-line options
    args = parse_args()

    # Initialize Grammar object
    grammar = Grammar(args.grammar_file)

    # Generate sentences
    for i in range(args.number_of_sentences):
        # Use Grammar object to generate sentence
        sentence = grammar.sample('ROOT',derivation_tree=args.tree, max_expansions=args.max_expansions)

        # Print the sentence with the specified format.
        # If it's a tree, we'll pipe the output through the prettyprint script.
        if args.tree:
            dict = str.maketrans({"\'": "", ",": "", "[": "(", "]": ")"})
            sentence = str(sentence).translate(dict)
            t = os.system(f"echo '{sentence}' | ./prettyprint")
        else:
            dict = str.maketrans({"\'": "", ",": "", "[": "", "]": ""})
            sentence = str(sentence).translate(dict)
            print(sentence)


if __name__ == "__main__":
    main()
