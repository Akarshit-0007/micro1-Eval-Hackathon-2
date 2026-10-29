from model.state import OverAllState
from utils.llm_utils import call_local_qwen

def llm_without_internal_files(state: OverAllState):
    print("Executing LLM without internal files node...")
    
    system_msg = (
        "You are an expert senior software developer and QA automation engineer. "
        "Note that no specific internal files or documents were provided for this query. "
        "Answer the user's question to the best of your ability using your general knowledge."
        "Donot Speak So much until ask "
    )
    
    # Call the dedicated utility function
    output_text = call_local_qwen(prompt=state.input, system_prompt=system_msg)
    
    # Return output to update graph state
    return {"output": output_text}