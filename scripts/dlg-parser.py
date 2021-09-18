# A script to parse Starship Titanic's *.dlg files, which contain the captions and wave files for dialogue.

from pathlib import Path

save_waves = False
in_dir = "<ENTER PATH HERE>/Assets/" # Path to the Starship Titanic "Assets" folder.
out_dir = "output/"

dialogue_files = [
    ["b310.dlg", "DeskBot"],
    ["c355.dlg", "BarBot"],
    ["c385.dlg", "Maitre d'Bot"],
    ["y456.dlg", "DoorBot"],
    ["y458.dlg", "BellBot"],
    ["z231.dlg", "LiftBot"],
    ["z451.dlg", "Succ-U-Bus"],
    ["z454.dlg", "Parrot"],
]

for file_index in range(len(dialogue_files)):
    in_file_path = in_dir + dialogue_files[file_index][0]
    
    bot_name = dialogue_files[file_index][1]

    with open(in_file_path, 'rb') as file:
        data = file.read()

    byte_count = len(data)

    file_size = int.from_bytes(data[0:4], byteorder='little', signed=False)

    pair_count = int.from_bytes(data[4:8], byteorder='little', signed=False)

    # Pairs consist of an ID and an offset.

    pairs_start = 8

    sentence_ids = []
    sentence_offsets = []
    wave_ids = []
    wave_offsets = []

    for i in range(pair_count):
        cur_pair_offset = pairs_start + i*8

        id = int.from_bytes(data[cur_pair_offset:cur_pair_offset+4], byteorder='little', signed=False)
        offset = int.from_bytes(data[cur_pair_offset+4:cur_pair_offset+8], byteorder='little', signed=False)

        # First pair is for a sentence, second is for its corresponding wave file, then they alternate.
        if i % 2 == 0:
            sentence_ids.append(id)
            sentence_offsets.append(offset)
        else:
            wave_ids.append(id)
            wave_offsets.append(offset)

    half_pair_count = int(pair_count / 2) # This is the number of sentences/wave files.

    base_file_name = Path(in_dir).stem

    # Save sentences file.
    out_path_sentences = f"{out_dir}sentences-{bot_name}.md"
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    with open(out_path_sentences, 'w') as file:

        file.write(f"# {bot_name}\n\n")
        file.write(f"This character has {str(half_pair_count)} sentences.\n\n")

        file.write("Index | Sentence ID | Wave ID | Sentence\n")
        file.write("--- | --- | --- | ---\n")

        for i in range(half_pair_count):
            start = sentence_offsets[i]
            end = wave_offsets[i]

            sentence_id = sentence_ids[i]
            wave_id = wave_ids[i]

            sentence = data[start:end].decode("ascii")

            file.write(f"{str(i)} | {sentence_id} | {wave_id} | {sentence}\n")

    if save_waves:
        # Save wave files.
        for i in range(half_pair_count):
            start = wave_offsets[i]

            if i < half_pair_count-1:
                end = sentence_offsets[i+1]
            else:
                end = file_size
            
            out_path = out_dir + base_file_name + "-" + str(i) + ".wav"
            with open(out_path, 'wb') as file:
                file.write(data[start:end])
