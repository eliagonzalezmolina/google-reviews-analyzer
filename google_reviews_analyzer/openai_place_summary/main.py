from openai_chat import OpenAIChat
from utils import build_place_summary_prompt

from google_reviews_analyzer.data_process.place_reviews import get_reviews_by_place
from google_reviews_analyzer.paths import data_dir
from google_reviews_analyzer.utils import load_config

# Load needed parameters
config = load_config()
place_name = config["openai_place_summary"]["data"]["place_name"]
input_path = f'{data_dir}/{config["openai_place_summary"]["data"]["input_path"]}'
output_path = f'{data_dir}/{config["openai_place_summary"]["data"]["output_path"]}'
api_key = config["OPEN_AI_API_KEY"]
engine_args = config["openai_place_summary"]["engine"]
model = engine_args["model"]
model_max_tokens = engine_args["model_max_tokens"]
temperature = engine_args["temperature"]
max_tokens = engine_args["max_tokens"]


# Load reviews for requested place
reviews = get_reviews_by_place(file_path=input_path, place_name=place_name)

# Build prompt
prompt = build_place_summary_prompt(
    place_name=place_name,
    reviews=reviews,
    model=model,
    model_max_tokens=model_max_tokens,
)

# Call OpenAI chatbot
chatbot = OpenAIChat(
    api_key=api_key, model=model, temperature=temperature, max_tokens=max_tokens
)
response = chatbot.chat(prompt)

with open(output_path, "w") as f:
    f.write(response)
