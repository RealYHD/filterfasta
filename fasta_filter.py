#!/usr/bin/env python3

import os
from Bio import SeqIO
import argparse


def main(args):
    kept_records = []
    for s_record in SeqIO.parse(args.input, "fasta"):
        if args.property != "all" and not (
                    args.contains in getattr(s_record, args.property)
                ):
            kept_records.append(s_record)
        elif args.property == "all" and not (
            args.contains in s_record.id
            or args.contains in s_record.name
                or args.contains in s_record.description):
            kept_records.append(s_record)
    SeqIO.write(
        kept_records,
        os.path.abspath(args.output),
        "fasta"
    )


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(
        "Removes sequences where id contains certain string.")
    argparser.add_argument(
        "input",
        type=str,
        metavar="i",
        help="The input fasta file."
    )

    argparser.add_argument(
        "output",
        type=str,
        metavar="o",
        help="The output file path."
    )

    argparser.add_argument(
        "-c",
        "--contains",
        type=str,
        default=None,
        required=False,
        help="The string to search for."
    )

    argparser.add_argument(
        "-p",
        "--property",
        type=str,
        default="all",
        required=False,
        help="""
        The part of the fasta file to look through. Valid options are: id,
        name, description, or all.
        """
    )

    main(argparser.parse_args())
