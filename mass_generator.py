import os

def expand_manual_files():
    input_folder = "cv_dataset"
    output_folder = "cv_dataset_expanded" # New separate folder
    
    # Create the new folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    nationalities = ["Italian", "Albanian", "Moroccan", "British"]
    genders = ["Male", "Female"]

    # This targets your files like MKT_JR_V1.txt (exactly 2 underscores)
    files_to_process = [f for f in os.listdir(input_folder) if f.count("_") == 2]

    count = 0
    for base_file in files_to_process:
        with open(os.path.join(input_folder, base_file), 'r', encoding='utf-8') as f:
            original_text = f.read()

        # Split the base name: MKT_JR_V1 -> ['MKT', 'JR', 'V1']
        parts = base_file.replace(".txt", "").split("_")
        
        for nat in nationalities:
            for gen in genders:
                # Create the 5-part filename for the pipeline
                # British = BR, Italian = IT, Albanian = AL, Moroccan = MO
                nat_code = "BR" if nat == "British" else nat[:2].upper()
                gen_code = gen[0].upper()
                
                # New filename: MKT_JR_BR_F_V1.txt
                new_filename = f"{parts[0]}_{parts[1]}_{nat_code}_{gen_code}_{parts[2]}.txt"
                
                # Replace the placeholders you wrote inside the text
                new_content = original_text.replace("[NATIONALITY]", nat).replace("[GENDER]", gen)
                
                # Save to the NEW folder
                with open(os.path.join(output_folder, new_filename), 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

    print(f"✅ Success! Generated {count} files in the '{output_folder}' folder.")

if __name__ == "__main__":
    expand_manual_files()