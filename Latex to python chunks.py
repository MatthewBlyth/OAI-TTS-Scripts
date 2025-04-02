import os
import pypandoc
import re
from TexSoup import TexSoup

# ----- Configuration -----
# Set the folder path containing your LaTeX files
folder_path = r"C:\Users\matth\Downloads\Superintelligence Strategy(2)\chapters"
# Output file for the python chunks
output_file = "output_chunks_expert_version_2.py"
# Maximum characters per chunk
max_chunk_size = 4000

# ----- Helper Functions -----
def clean_latex(latex_content):
    """
    Uses TexSoup to parse the LaTeX content and remove unwanted elements,
    such as citation commands and figure/table environments.
    """
    soup = TexSoup(latex_content)
    
    # Remove common citation commands
    citation_commands = ['cite', 'citet', 'citep', 'citealt', 'citealp']
    for cmd in citation_commands:
        for tag in soup.find_all(cmd):
            latex_content = latex_content.replace(str(tag), '')
    
    # Remove environments for figures, tables, and similar
    envs_to_remove = ['figure', 'table', 'tabular']
    for env in envs_to_remove:
        while f"\\begin{{{env}}}" in latex_content:
            start = latex_content.find(f"\\begin{{{env}}}")
            end = latex_content.find(f"\\end{{{env}}}", start)
            if end == -1:
                break  # unmatched environment; exit loop
            latex_content = latex_content[:start] + latex_content[end + len(f"\\end{{{env}}}"):]
    
    return latex_content

def convert_to_plain_text(latex_content):
    """
    Uses pypandoc to convert cleaned LaTeX to plain text.
    """
    try:
        plain_text = pypandoc.convert_text(latex_content, 'plain', format='latex')
        if not plain_text.strip():
            print("Warning: Conversion produced an empty result.")
    except Exception as e:
        print("Error during conversion with pypandoc:", e)
        plain_text = ""
    return plain_text

def reflow_text(text):
    """
    Reflows text by joining lines that belong to the same paragraph.
    Lines separated by a blank line are considered separate paragraphs.
    """
    paragraphs = []
    current_paragraph = []
    for line in text.splitlines():
        if line.strip():
            current_paragraph.append(line.strip())
        else:
            if current_paragraph:
                paragraphs.append(" ".join(current_paragraph))
                current_paragraph = []
    if current_paragraph:
        paragraphs.append(" ".join(current_paragraph))
    return "\n\n".join(paragraphs)

def chunk_text(text, max_size):
    """
    Splits the reflowed text into chunks less than max_size characters,
    ensuring each chunk ends at a paragraph boundary.
    """
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""
    for para in paragraphs:
        candidate = current_chunk + ("\n\n" if current_chunk else "") + para
        if len(candidate) > max_size:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = para
            else:
                # Paragraph alone exceeds the limit; split it arbitrarily.
                while len(para) > max_size:
                    chunks.append(para[:max_size])
                    para = para[max_chunk_size:]
                current_chunk = para
        else:
            current_chunk = candidate
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def post_process_text(text):
    """
    Performs additional cleaning on the text:
      1. For each line, if the line (after trimming) does not end with a colon, semicolon, or period,
         append a period.
      2. Replace any single-word acronym in parentheses with 'or <ACRONYM>'.
    """
    processed_lines = []
    for line in text.splitlines():
        stripped = line.rstrip()
        if stripped and stripped[-1] not in (':', ';', '.'):
            stripped += '.'
        processed_lines.append(stripped)
    new_text = "\n".join(processed_lines)
    
    # Replace single-word acronyms in parentheses (e.g. (MAIM) -> or MAIM)
    # This regex only matches if there is exactly one word (all uppercase) inside the parentheses.
    new_text = re.sub(r'\(([A-Z]{2,})\)', r'or \1', new_text)
    
    return new_text

# ----- Main Processing -----
all_text = ""

# Process each LaTeX file in the folder
for filename in sorted(os.listdir(folder_path)):
    if filename.lower().endswith(".tex"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            latex_content = file.read()
        cleaned_latex = clean_latex(latex_content)
        plain_text = convert_to_plain_text(cleaned_latex)
        all_text += plain_text + "\n"

# Reflow the text to join lines within paragraphs
reflowed_text = reflow_text(all_text)
# Chunk the reflowed text ensuring paragraph breaks are preserved
chunks = chunk_text(reflowed_text, max_chunk_size)
# Apply post-processing to each chunk
chunks = [post_process_text(chunk) for chunk in chunks]

# ----- Write to Output Python File -----
with open(output_file, 'w', encoding='utf-8') as out_file:
    for idx, chunk in enumerate(chunks, start=1):
        out_file.write(f"text_{idx} = (\n")
        # Write each processed line as a separate string literal with an explicit \n.
        for line in chunk.splitlines():
            safe_line = line.replace('"', '\\"')
            out_file.write(f'    "{safe_line}\\n"\n')
        out_file.write(")\n\n")

print(f"Processing complete. {len(chunks)} chunks written to {output_file}.")




