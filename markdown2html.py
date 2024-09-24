#!/usr/bin/python3
"""
markdown2html.py - Convert Markdown file to HTML file.
Usage: ./markdown2html.py <input_file> <output_file>
Arguments:
<input_file>: Path to the input Markdown file.
<output_file>: Path to the output HTML file.
Examples:
$ ./markdown2html.py
Usage: ./markdown2html.py <input_file> <output_file>
$ ./markdown2html.py bla.md
Missing bla.md
$ ./markdown2html.py bla.md blu.html
"""
import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Converts a Markdown file to HTML.
    Args:
    input_file (str): Path to the input Markdown file.
    output_file (str): Path to the output HTML file.
    Returns:
    None
    """
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Check if the input Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read Markdown content from input file
    with open(input_file, 'r') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    # Write HTML content to output file
    with open(output_file, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    # Ensure correct usage with two arguments
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)
    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)