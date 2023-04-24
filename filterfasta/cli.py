#!/usr/bin/env python3

import os
from Bio import SeqIO
import argparse


def filter(input: str, a_property: str, contains: str):
    kept_records = []
    for s_record in SeqIO.parse(input, "fasta"):
        if a_property != "all" and not (contains in getattr(s_record, a_property)):
            kept_records.append(s_record)
        elif a_property == "all" and not (
            contains in s_record.id
            or contains in s_record.name
            or contains in s_record.description
        ):
            kept_records.append(s_record)
    return kept_records


def write_to_fasta(kept_records, output: str):
    SeqIO.write(kept_records, os.path.abspath(output), "fasta")


def run(args):
    kept = filter(args.input, args.property, args.contains)
    write_to_fasta(kept, args.output)


def main():
    argparser = argparse.ArgumentParser(
        "Removes sequences where id contains certain string."
    )
    argparser.add_argument("input", type=str, metavar="i", help="The input fasta file.")

    argparser.add_argument(
        "output", type=str, metavar="o", help="The output file path."
    )

    argparser.add_argument(
        "-c",
        "--contains",
        type=str,
        default=None,
        required=False,
        help="The string to search for.",
    )

    argparser.add_argument(
        "-p",
        "--property",
        type=str,
        default="all",
        required=False,
        help="""
        The part of the fasta file to look through. Valid options are: 'id',
        'name', 'description', or 'all'.
        """,
    )
    args = argparser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
