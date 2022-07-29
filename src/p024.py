### Mail merge ###

from pathlib import Path

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

src_path = Path(__file__).parent

with (src_path / "./res024input/Names/invited_names.txt").open() as f:
    names = [name.strip() for name in f.readlines()]

for name in names:
    with (src_path / "./res024input/Letters/starting_letter.txt").open() as f:
        with (src_path / f"./res024output/ReadyToSend/letter_to_{name}.txt").open(
            "w"
        ) as w:
            for line in f:
                w.write(line.replace("[name]", name))
