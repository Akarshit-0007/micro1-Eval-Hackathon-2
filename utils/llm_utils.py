import os
import ollama

def call_local_qwen(
    prompt: str, file_paths: list[str] = None,system_prompt: str = "You are an expert senior in the Domain regarding Question ask."
) -> str:
    """Unified utility to call local Qwen via Ollama with optional file context and streaming."""
    
    # 1. Conditionally append file contents if file_paths exist
    full_prompt = prompt
    if file_paths:
        context_text = "\n\n--- PROVIDED INTERNAL FILES ---\n"
        for path in file_paths:
            if os.path.exists(path):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        file_content = f.read()
                    context_text += f"\nFile: `{path}`\n```\n{file_content}\n```\n"
                except Exception as e:
                    context_text += f"\nFile: `{path}` (Error reading file: {e})\n"
            else:
                context_text += f"\nFile: `{path}` (Path not found)\n"
        full_prompt = f"{prompt}{context_text}"

    # 2. Configure model parameters
    model_options = {
        "temperature": 0.7,
        "top_p": 0.9,
        "num_ctx": 8192,
        "presence_penalty": 1.5,
    }

    print(f"--- Sending prompt to local Qwen 3.5 ---\nPrompt: {prompt}\n")
    if file_paths:
        print(f"Attached Files: {file_paths}\n")
    print("--- Response ---")

    full_response = ""
    try:
        # 3. Stream response from local Ollama instance
        stream = ollama.chat(
            model='qwen3.5:4b',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': full_prompt},
            ],
            options=model_options,
            stream=True,
        )

        for chunk in stream:
            content = chunk['message']['content']
            print(content, end='', flush=True)
            full_response += content
            
        print("\n\n--- Execution Complete ---")

    except Exception as e:
        error_msg = f"\nError communicating with local Ollama instance: {e}"
        print(error_msg)
        print("Make sure Ollama is running in the background (run 'ollama serve').")
        full_response = error_msg

    return full_response