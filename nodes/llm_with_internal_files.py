from model.state import OverAllState
from utils.llm_utils import call_local_qwen

def llm_with_internal_files(state: OverAllState):
    system_msg = (
        "You are an expert senior software developer and QA automation engineer. "
        "Analyze the provided internal files carefully to answer the user query."
        "Donot Speak So much until ask "
    )
    
    # Call utility WITH files
    output_text = call_local_qwen(prompt=state.input, file_paths=state.files, system_prompt=system_msg)
    
    return {"output": output_text}