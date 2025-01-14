import re
from typing import List

def split_text_with_ansi(text: str, width: int) -> List[str]:
    """
    Split text with ANSI codes into lines of specified width.

    Args:
        text: Input text with ANSI codes.
        width: Maximum line width.

    Returns:
        List of lines with ANSI codes preserved.
    """
    # Regex to match ANSI codes and regular text
    pattern = re.compile(r'(\033\[[0-9;]*m|[^\033]+)')

    # Split text into segments (ANSI codes and regular text)
    segments = pattern.findall(text)
    clean_text = ''.join(seg for seg in segments if not seg.startswith("\033"))
    words = clean_text.split()

    # Wrap words while respecting the width
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) + 1 > width:
            lines.append(current_line)
            current_line = word
        else:
            current_line += (' ' if current_line else '') + word
    if current_line:
        lines.append(current_line)

    # Reconstruct lines with ANSI codes
    wrapped_lines = []
    for line in lines:
        reconstructed_line = ''
        for segment in segments:
            if not line:
                break
            if segment.startswith("\033"):
                reconstructed_line += segment
            else:
                # Consume characters from the line
                to_add = segment[:len(line)]
                line = line[len(to_add):]
                reconstructed_line += to_add
        wrapped_lines.append(reconstructed_line)

    return wrapped_lines
