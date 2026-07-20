# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://chat-ai-agent-resource.services.ai.azure.com/api/projects/chat-ai-agent"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "computing-historian"
my_version = "1"

openai_client = project_client.get_openai_client()

while True:
    prompt = input("Enter a prompt for the agent (or type 'quit' to exit): ").strip()
    if prompt.lower() == "quit":
        print("Exiting.")
        break
    if not prompt:
        print("Please enter a non-empty prompt or type 'quit'.")
        continue

    response = openai_client.responses.create(
        input=[{"role": "user", "content": prompt}],
        extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
    )

    print(f"Response output: {response.output_text}\n")



