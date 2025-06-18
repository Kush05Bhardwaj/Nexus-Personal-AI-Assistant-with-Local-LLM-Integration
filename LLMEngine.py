from llama_cpp import Llama

# Lazy loaded model instance
llm = None

def get_model():
    global llm
    if llm is None:
        try:
            print("Loading LLM model...")
            llm = Llama(
                model_path="C:/Nexus/models/openhermes-2.5-mistral-7b.Q4_K_M.gguf",
                n_ctx=4096
            )
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise e
    return llm

SYSTEM_PROMPT = """
You are Nexus, a friendly AI voice assistant who speaks casually like a human.
You keep your answers short, natural, and engaging. Avoid being too formal.
When asked questions, you answer in a friendly tone.
"""

def format_prompt(user_prompt):
    return f"[INST] <<SYS>>\n{SYSTEM_PROMPT}\n<</SYS>>\n{user_prompt} [/INST]"


def query_llm(prompt):
    model = get_model()
    try:
        response = model(
            prompt=format_prompt(prompt),
            max_tokens=512,
            temperature=0.7,
            top_p=0.9
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        print(f"LLM generation error: {e}")
        return "Sorry, I was unable to process that."
