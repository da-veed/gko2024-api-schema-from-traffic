import os
import json
import argparse
from dotenv import load_dotenv
import openai

from src.consts.directories import CONFIG_DIR, ROOT_DIR

load_dotenv(ROOT_DIR / ".env")

openai.api_type = os.environ.get("OPENAI__API_TYPE")
openai.api_base = os.environ.get("OPENAI__API_BASE")
openai.api_key = os.environ.get("OPENAI__API_KEY")
openai.api_version = os.environ.get("OPENAI__API_VERSION")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--message",
        type=str,
        default="tell me a joke",
        help="message passed to the ChatGPT model",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="chatgpt_001.json",
        help="ChatGPT config name passed to the model",
    )
    cfg = parser.parse_args()
    return cfg


def main() -> str:
    cfg = parse_args()
    with open(CONFIG_DIR / cfg.config) as fp_out:
        message_config = json.load(fp_out)

    # launch Azure ChatGPT model
    message_config["messages"].append({"role": "user", "content": cfg.message})
    model_response = openai.ChatCompletion.create(**message_config)

    output_text = model_response.choices[0].message.content

    print(output_text)

    return output_text


if __name__ == "__main__":
    main()
