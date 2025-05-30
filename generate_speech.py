import os
import html2text
from pathlib import Path
from openai import OpenAI
from datetime import datetime
from markdown import markdown
from dotenv import load_dotenv

# Load environment variables from local.env file
load_dotenv(dotenv_path=".env")
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found.")

client = OpenAI(api_key=api_key)

# === CONFIGURATION ===
section_name = "intro"  # Change this to the section name to include in the filename
voice = "onyx"         
instructions = "Speak in a confident and professional tone, suitable for a product demo."

# Read input text from Markdown file
input_text_file = Path("input_markdown.md")
if not input_text_file.exists():
    raise FileNotFoundError(f"Input text file not found: {input_text_file}")
markdown_content = input_text_file.read_text()

# Convert Markdown to plain text using html2text
html_content = markdown(markdown_content, output_format="html")  # Render Markdown to HTML
text_converter = html2text.HTML2Text()
text_converter.ignore_links = True  # Optional: Ignore links in the output
input_text = text_converter.handle(html_content)

# === TIMESTAMPED FILENAME HANDLING ===
output_dir = Path("voiceovers")
output_dir.mkdir(parents=True, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
base_filename = f"{section_name}_{timestamp}"
speech_file_path = output_dir / f"{base_filename}.mp3"

# Prevent duplicates if run multiple times in the same minute
counter = 1
while speech_file_path.exists():
    speech_file_path = output_dir / f"{base_filename}_{counter:02}.mp3"
    counter += 1

# === GENERATE SPEECH ===
response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice=voice,
    input=input_text,
    instructions=instructions,
    response_format="mp3"
)

with open(speech_file_path, "wb") as f:
    f.write(response.content)

print(f"✅ Speech saved as: {speech_file_path}")