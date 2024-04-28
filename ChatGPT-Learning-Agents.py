from openai import OpenAI

client = OpenAI(api_key='hidden_key')

def get_gpt_response(question):
      # Replace with your actual API key

    try:
        response = client.completions.create(model="text-davinci-003",  # or another model you prefer
        prompt=question,
        max_tokens=300)
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Prepare a list of questions
questions = [
    "What is the definition of an agent in machine learning?",
    "What are the main components of an agent in machine learning?",
    "What are the different types of agents in machine learning?",
    "Can you provide examples of agent-based machine learning algorithms?"
]

# Interact with ChatGPT and record responses
for question in questions:
    response = get_gpt_response(question)
    print(f"Question: {question}")
    print(f"Response: {response}")
    print("\n" + "-"*50 + "\n")
