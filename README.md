# markdown-to-speech

markdown-to-speech is a Python tool that converts Markdown text into high-quality voiceovers using OpenAI's text-to-speech API. This tool is ideal for creating professional audio content from structured text files.

## Features

- Converts Markdown files to plain text.
- Generates speech in MP3 format using OpenAI's text-to-speech API.
- Customizable voice and tone settings.
- Automatically timestamps filenames to prevent overwriting.

## Requirements

- Python 3.8 or higher
- OpenAI Python SDK
- Required Python libraries:
  - `html2text`
  - `markdown`
  - `python-dotenv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/markdown-to-speech.git
   cd markdown-to-speech
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root.
   - Add the following line to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Place your Markdown file in the project directory and name it `input_text.md`.

2. Run the script:

   ```bash
   python generate_speech.py
   ```

3. The generated MP3 file will be saved in the `voiceovers` directory with a timestamped filename.

## Configuration

You can customize the following settings in `generate_speech.py`:

- **Section Name:** Change the `section_name` variable to include a specific section name in the filename.
- **Voice:** Modify the `voice` variable to use a different voice model (e.g., `onyx`, `jade`, etc.).
- **Instructions:** Update the `instructions` variable to adjust the tone and style of the speech.

## Example Output

After running the script, you will see a confirmation message:

```
✅ Speech saved as: voiceovers/intro_2025-05-30_14-45.mp3
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Feel free to submit issues or pull requests to improve this tool!

````# Markdown-to-Speech

Markdown-to-Speech is a Python tool that converts Markdown text into high-quality voiceovers using OpenAI's text-to-speech API. This tool is ideal for creating professional audio content from structured text files.

## Features
- Converts Markdown files to plain text.
- Generates speech in MP3 format using OpenAI's text-to-speech API.
- Customizable voice and tone settings.
- Automatically timestamps filenames to prevent overwriting.

## Requirements
- Python 3.8 or higher
- OpenAI Python SDK
- Required Python libraries:
  - `html2text`
  - `markdown`
  - `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/markdown-to-speech.git
   cd markdown-to-speech
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root.
   - Add the following line to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

1. Place your Markdown file in the project directory and name it `input_text.md`.

2. Run the script:

   ```bash
   python generate_speech.py
   ```

3. The generated MP3 file will be saved in the `voiceovers` directory with a timestamped filename.

## Configuration

You can customize the following settings in `generate_speech.py`:

- **Section Name:** Change the `section_name` variable to include a specific section name in the filename.
- **Voice:** Modify the `voice` variable to use a different voice model (e.g., `onyx`, `jade`, etc.).
- **Instructions:** Update the `instructions` variable to adjust the tone and style of the speech.

## Example Output

After running the script, you will see a confirmation message:

```
✅ Speech saved as: voiceovers/intro_2025-05-30_14-45.mp3
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Feel free to submit issues or pull requests to improve this tool!
