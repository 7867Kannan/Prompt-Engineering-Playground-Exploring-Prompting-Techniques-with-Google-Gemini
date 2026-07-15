"""
prompt_templates.py

This module demonstrates common prompt engineering techniques.
Each function returns a prompt that can be sent directly to an LLM
such as Gemini, GPT, Claude, or Llama.

Author: Your Name
"""

# ------------------------------------------------------------
# 1. Zero-Shot Prompting
# ------------------------------------------------------------

def zero_shot(prompt):
    return f"""
You are a knowledgeable AI assistant.

Task:
{prompt}

Instructions:
- Answer directly.
- Use simple English.
- Be accurate and concise.
"""


# ------------------------------------------------------------
# 2. One-Shot Prompting
# ------------------------------------------------------------

def one_shot(prompt):
    return f"""
You are a knowledgeable AI assistant.

Example

Question:
What is Cloud Computing?

Answer:

Definition:
Cloud Computing is the delivery of computing services over the Internet.

Key Points:
- No physical servers required
- Accessible from anywhere
- Pay only for what you use

Example:
Google Drive, AWS, Microsoft Azure

--------------------------------------------------

Now answer the following question in the same format.

Question:
{prompt}
"""


# ------------------------------------------------------------
# 3. Few-Shot Prompting
# ------------------------------------------------------------

def few_shot(prompt):
    return f"""
You are a knowledgeable AI assistant.

Follow the examples below.

==================================================

Example 1

Question:
What is Artificial Intelligence?

Answer:

Definition:
Artificial Intelligence (AI) enables computers to perform tasks that normally require human intelligence.

Key Points:
- Learns from data
- Makes decisions
- Solves problems

Example:
ChatGPT, Siri

Summary:
AI makes machines intelligent.

==================================================

Example 2

Question:
What is Machine Learning?

Answer:

Definition:
Machine Learning is a branch of AI where computers learn from data.

Key Points:
- Uses datasets
- Finds patterns
- Improves over time

Example:
Netflix Recommendation System

Summary:
Machine Learning allows computers to learn automatically.

==================================================

Now answer the following.

Question:
{prompt}
"""


# ------------------------------------------------------------
# 4. Role Prompting
# ------------------------------------------------------------

def role_prompt(prompt):
    return f"""
You are an experienced Computer Science professor with over 20 years of teaching experience.

Your teaching style should be:

- Beginner-friendly
- Simple English
- Practical
- Well-organized

While answering:

1. Definition
2. Explanation
3. Three key points
4. Real-world example
5. Practical application
6. Short summary

Question:

{prompt}
"""


# ------------------------------------------------------------
# 5. Chain-of-Thought Prompting
# ------------------------------------------------------------

def chain_of_thought(prompt):
    return f"""
You are an expert problem solver.

Solve the following problem step by step.

Instructions:

1. Identify the given information.
2. Explain the solution process.
3. Perform calculations if needed.
4. Verify the result.
5. Provide the final answer.

Problem:

{prompt}
"""


# ------------------------------------------------------------
# 6. Structured Prompting
# ------------------------------------------------------------

def structured_prompt(prompt):
    return f"""
Answer the following topic using exactly this structure.

Definition

Explanation

Advantages

Disadvantages

Applications

Real-world Example

Summary

Topic:

{prompt}
"""


# ------------------------------------------------------------
# 7. Contextual Prompting
# ------------------------------------------------------------

def contextual_prompt(prompt):
    return f"""
Context:

You are helping a final-year engineering student prepare for campus placements.
The student prefers simple explanations with practical examples.

Task:

{prompt}

Instructions:

- Use beginner-friendly language.
- Give practical examples.
- Highlight interview points.
"""


# ------------------------------------------------------------
# 8. Instruction Prompting
# ------------------------------------------------------------

def instruction_prompt(prompt):
    return f"""
Complete the following task by following every instruction carefully.

Task:

{prompt}

Requirements:

- Use clear English.
- Keep the answer under 250 words.
- Use bullet points wherever appropriate.
- End with a one-line conclusion.
"""


# ------------------------------------------------------------
# 9. Output Format Prompting
# ------------------------------------------------------------

def output_format_prompt(prompt):
    return f"""
Answer the following question.

Question:
{prompt}

Return the answer using this format.

Definition:
...

Key Points:
- ...
- ...
- ...

Example:
...

Summary:
...
"""


# ------------------------------------------------------------
# 10. Constraint Prompting
# ------------------------------------------------------------

def constraint_prompt(prompt):
    return f"""
Answer the following question.

Question:
{prompt}

Constraints:

- Maximum 100 words
- Use only simple English
- Do not use technical jargon
- Give one real-world example
"""


# ------------------------------------------------------------
# 11. Persona + Context Prompting
# ------------------------------------------------------------

def persona_context_prompt(prompt):
    return f"""
You are a senior Software Engineer at Google.

You are mentoring a fresher who has basic programming knowledge.

Explain the following topic.

Topic:
{prompt}

Requirements:

- Start with a simple definition.
- Explain as if teaching a beginner.
- Give an industry example.
- Mention one interview question related to the topic.
"""


# ------------------------------------------------------------
# 12. Comparative Prompting
# ------------------------------------------------------------

def comparative_prompt(prompt):
    return f"""
Compare the following concepts.

Topic:

{prompt}

Use the following format.

Definition

Similarities

Differences

Advantages

Disadvantages

Applications

Conclusion
"""


# ------------------------------------------------------------
# 13. Reflection Prompting
# ------------------------------------------------------------

def reflection_prompt(prompt):
    return f"""
Answer the following question.

Question:
{prompt}

After answering, review your own response.

Then provide:

1. Strengths of your answer
2. Possible improvements
3. Final improved answer
"""


# ------------------------------------------------------------
# 14. Retrieval-Augmented Prompting (RAG Style)
# ------------------------------------------------------------

def rag_prompt(context, question):
    return f"""
Use ONLY the information provided in the context below.

If the answer is not available in the context,
reply:

"I cannot find the answer in the provided context."

Context:

{context}

Question:

{question}
"""
