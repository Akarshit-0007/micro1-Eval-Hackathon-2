from model.state import OverAllState
import os

def load_dataset_node(state: OverAllState):
    print(state.input)
    files = state.files
    if not files:
        print("No files provided. Proceeding to LLM node...")
        return {"contain_files": False}
    
    # Otherwise, check all provided files
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"Error: File not found -> {file_path}")
            raise ValueError(f'Error: File not found -> {file_path}')
            
        else:
            print(f"Found: {file_path}")
            
    # All files exist
    return {"contain_files": True}