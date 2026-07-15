from google import genai
from dotenv import load_dotenv
import os

from prompt_templates import *

# ==========================================================
# Load Gemini API Key
# ==========================================================

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================================
# Prompt Templates Dictionary
# ==========================================================

templates = {
    1: zero_shot,
    2: one_shot,
    3: few_shot,
    4: role_prompt,
    5: chain_of_thought,
    6: structured_prompt,
    7: contextual_prompt,
    8: instruction_prompt,
    9: output_format_prompt,
    10: constraint_prompt,
    11: persona_context_prompt,
    12: comparative_prompt,
    13: reflection_prompt,
}

# ==========================================================
# Save Prompt History
# ==========================================================

def save_history(prompt_type, user_prompt, response):
    with open("history.txt", "a", encoding="utf-8") as file:
        file.write("\n")
        file.write("=" * 80 + "\n")
        file.write(f"PROMPT TYPE : {prompt_type}\n\n")
        file.write("USER PROMPT:\n")
        file.write(user_prompt + "\n\n")
        file.write("AI RESPONSE:\n")
        file.write(response + "\n")
        file.write("=" * 80 + "\n")


# ==========================================================
# Main Program
# ==========================================================

while True:

    print("\n")
    print("=" * 65)
    print("          PROMPT ENGINEERING PLAYGROUND")
    print("=" * 65)

    print(" 1. Zero-Shot Prompting")
    print(" 2. One-Shot Prompting")
    print(" 3. Few-Shot Prompting")
    print(" 4. Role Prompting")
    print(" 5. Chain-of-Thought Prompting")
    print(" 6. Structured Prompting")
    print(" 7. Contextual Prompting")
    print(" 8. Instruction Prompting")
    print(" 9. Output Format Prompting")
    print("10. Constraint Prompting")
    print("11. Persona + Context Prompting")
    print("12. Comparative Prompting")
    print("13. Reflection Prompting")
    print("14. Exit")

    try:
        choice = int(input("\nSelect an option (1-14): "))
    except ValueError:
        print("\nPlease enter a valid number.")
        continue

    if choice == 14:
        print("\nThank you for using Prompt Engineering Playground.")
        break

    if choice not in templates:
        print("\nInvalid choice. Please try again.")
        continue

    user_prompt = input("\nEnter your prompt:\n\n")

    # Generate Prompt
    final_prompt = templates[choice](user_prompt)

    try:
        response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=final_prompt,
)

        answer = response.text

        print("\n")
        print("=" * 65)
        print("AI RESPONSE")
        print("=" * 65)
        print(answer)

        save_history(
            templates[choice].__name__,
            user_prompt,
            answer
        )

        print("\nPrompt history saved successfully.")

    except Exception as e:
        print("\nError while calling Gemini API.")
        print(e)
