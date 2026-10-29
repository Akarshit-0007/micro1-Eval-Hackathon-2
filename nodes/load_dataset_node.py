from model.state import OverAllState
import os

def load_dataset_node(state: OverAllState):
    print(state.input)
    files = state.files
    for file_path in files:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
        else:
            print('found')


    return