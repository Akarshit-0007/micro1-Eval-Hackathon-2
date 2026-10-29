import ollama

def run_local_qwen():
    # Define model generation options/parameters
    model_options = {
        "temperature": 0.7,      # Controls randomness (higher = more creative, lower = more deterministic)
        "top_p": 0.9,            # Nucleus sampling parameter
        "num_ctx": 8192,         # Context window size allocation
        "presence_penalty": 1.5, # Reduces text repetition
    }

    prompt = "What is Java"

    print(f"--- Sending prompt to local Qwen 3.5 ---\nPrompt: {prompt}\n")
    print("--- Response ---")

    try:
        # Using streaming mode so output prints chunk-by-chunk in real time
        stream = ollama.chat(
            model='qwen3.5:4b',  # <-- Updated to match the pulled tag
            messages=[
                {
                    'role': 'system', 
                    'content': 'You are an expert senior software developer and QA automation engineer.'
                },
                {
                    'role': 'user', 
                    'content': prompt
                },
            ],
            options=model_options,
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            
        print("\n\n--- Execution Complete ---")

    except Exception as e:
        print(f"\nError communicating with local Ollama instance: {e}")
        print("Make sure Ollama is running in the background (run 'ollama serve').")

if __name__ == "__main__":
    run_local_qwen()