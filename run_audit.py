import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util

# 1. Initialize the S-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')
print(model)
def run_thesis_audit():
    # Define folder paths as shown in your VS Code screenshot
    jd_folder = "job_descriptions"
    cv_folder = "cv_dataset_expanded"
    results_folder = "results"

    # Pre-load all Job Descriptions into a dictionary for speed
    jds = {}
    for f in os.listdir(jd_folder):
        if f.endswith(".txt"):
            with open(os.path.join(jd_folder, f), 'r', encoding='utf-8') as file:
                jds[f] = file.read()

    results = []
    
    # Get all the generated CV files
    cv_files = [f for f in os.listdir(cv_folder) if f.endswith(".txt")]
    print(f"Starting audit on {len(cv_files)} files...")

    for cv_file in cv_files:
        # Split: MKT_JR_IT_M_V1.txt -> ['MKT', 'JR', 'IT', 'M', 'V1']
        parts = cv_file.replace(".txt", "").split("_")
        
        # Match CV to JD (e.g., JD_MKT_JR.txt)
        jd_key = f"JD_{parts[0]}_{parts[1]}.txt"
        
        if jd_key in jds:
            with open(os.path.join(cv_folder, cv_file), 'r', encoding='utf-8') as f:
                cv_text = f.read()
            
            # Calculate Semantic Similarity
            emb_jd = model.encode(jds[jd_key], convert_to_tensor=True)
            emb_cv = model.encode(cv_text, convert_to_tensor=True)
            print(emb_cv)
            print(emb_jd)
            score = util.cos_sim(emb_jd, emb_cv).item()
            
            # Extract and store metadata
            results.append({
                "Job": parts[0],
                "Level": parts[1],
                "Nationality": parts[2],
                "Gender": parts[3],
                "Version": parts[4],
                "Similarity_Score": round(score, 4),
                "Filename": cv_file,
                "JD_Filename": jd_key
            })

    # Save to the 'results' folder
    df = pd.DataFrame(results)
    output_file = os.path.join(results_folder, "final_bias_audit_results.csv")
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Results saved in {output_file}")

if __name__ == "__main__":
    run_thesis_audit()