# Fasta Filter

A simple program to remove sequences in a fasta file containing specific strings.

## Usage

 0. Install python3.

 1. Run `pip install -r ./requirements.txt` if `biopython` is not installed. If installed, skip to step 2.

 2. Run `./fasta_filter.py -h` if on Linux, or on Windows `python3 ./fasta_filter -h`. See help for more information.

### Example Usage

 1. Pretend `input.fasta` exists in the same folder as `fasta_filter.py` (the program file).

 2. To remove all sequences in `input.fasta` that contain `rt` in the header and output to a new file called `input_filtered.fasta`, run: `python3 ./fasta_filter.py input.fasta input_filtered.fasta -c rt`

