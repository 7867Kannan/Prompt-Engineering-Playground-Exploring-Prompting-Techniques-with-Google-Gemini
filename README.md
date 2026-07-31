# Prompt Engineering Playground

A Python CLI tool for designing, testing, and generating prompts for AI models using Google Gemini.

## What this project does

- Provides a command-line interface to choose from 13 prompt engineering strategies.
- Sends prompt templates to Google Gemini using the `google-genai` SDK.
- Logs user prompts and AI responses to `history.txt` for review and improvement.
- Keeps API credentials secure using a `.env` file and `python-dotenv`.

## Key features

- 13 reusable prompt templates:
  - `zero_shot`
  - `one_shot`
  - `few_shot`
  - `role_prompt`
  - `chain_of_thought`
  - `structured_prompt`
  - `contextual_prompt`
  - `instruction_prompt`
  - `output_format_prompt`
  - `constraint_prompt`
  - `persona_context_prompt`
  - `comparative_prompt`
  - `reflection_prompt`
- Easy selection via CLI menu with 14 choices.
- AI response persistence for evaluation and playback.
- Clear prompt formatting for consistent AI behavior.

## Tech stack

- Python
- Google Gemini via `google-genai`
- Environment configuration via `python-dotenv`

## Setup

1. Clone or download the project files.
2. Create a `.env` file in the project root with your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

3. Install dependencies:

```bash
pip install -r requirement.txt
```

## Usage

Run the main program:

```bash
python main.py
```

Then:

1. Select the prompt strategy number.
2. Enter your prompt text.
3. View the AI-generated answer.
4. Check `history.txt` for saved prompt/response history.

## Project structure

- `main.py` — CLI entrypoint and Gemini API integration.
- `prompt_templates.py` — prompt template library for 13 prompt types.
- `model_availability.py` — example Gemini model listing utility.
- `history.txt` — saved interaction history.
- `requirement.txt` — project dependencies.

## Resume-ready highlights

- Built a prompt engineering playground supporting 13 AI prompt strategies.
- Integrated Google Gemini API with secure `.env` credential handling.
- Implemented prompt history logging for model evaluation and iterative refinement.
- Modularized prompt templates separately from runtime logic.

## Notes

- Replace `your_api_key_here` with your actual Gemini API key.
- Update `model="models/gemini-3.5-flash"` in `main.py` if you want a different Gemini model.
- Use `history.txt` to review prompt effectiveness and refine prompt design.
