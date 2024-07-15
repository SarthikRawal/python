# 9. Write a Python program to display formatted text (width=50) as output.

# using textwrap
# import textwrap

# def format_text(text, width):
#     wrapped_text = textwrap.fill(text, width)
#     return wrapped_text

def formated_text(s, width):
    formatted_text = ""
    line = ""
    for word in s.split():
        if len(line + word) + 1 <= width:
            line += word + " "
        else:
            formatted_text += line.rstrip() + "\n"
            line = word + " "
    if line:
        formatted_text += line.rstrip()
    return formatted_text

input_string = "This is an example of a very long string that needs to be formatted with a width of fifty characters."
width = 50
print(formated_text(input_string, width))