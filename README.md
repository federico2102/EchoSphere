
---

# Conversational AI Voice Interaction Project

A Python-based project that brings together natural language generation, speech synthesis, and voice recognition to simulate a conversational AI system. Designed with modularity in mind, this project can easily be expanded with alternative language models (both free and paid) for enhanced performance. Perfect for showcasing skills in machine learning integration, API utilization, and real-time conversational applications.

## Project Overview

This Conversational AI project allows multiple "AIs" to engage in natural-sounding dialogue, each with unique voices, creating an immersive, podcast-like experience. It combines:
- **Natural Language Processing (NLP)** for generating human-like responses.
- **Speech Synthesis** to produce distinctive, lifelike voices.
- **Speech Recognition** to convert generated audio back into text as needed.
  
Designed for flexibility, the project can be configured to use offline models like GPT-Neo or GPT-J. It also supports an easy switch to paid APIs (e.g., OpenAI’s GPT-3) for improved response quality.

## Main Features

- **Real-Time Conversation**: Two or more distinct AIs take turns generating responses, creating a back-and-forth dialogue.
- **Distinct Voices for Each AI**: Each AI character speaks in its own unique voice, ensuring clear distinction without labels.
- **Offline Model Support**: Includes setup for using open-source language models like GPT-Neo, with optional configurations for larger models like GPT-J.
- **API Integration Ready**: With a few configuration changes, you can incorporate paid NLP APIs like OpenAI's GPT-3 for faster, more sophisticated responses.
- **Modular Design**: Easily extendable components for speech-to-text, text-to-speech, and language generation, allowing experimentation with different models or APIs.

## Setup Guide

### Prerequisites

1. **Python 3.8+** and **Pip**: Make sure Python and Pip are installed.
2. **Virtual Environment**: Recommended to create a virtual environment for dependencies.
3. **Google Cloud API Key**: For text-to-speech and speech-to-text functionality, set up a Google Cloud account and enable the Text-to-Speech and Speech-to-Text APIs. [Google Cloud Documentation](https://cloud.google.com/docs)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/federico2102/EchoSphere.git
   cd EchoSphere
   ```

2. **Set Up Environment and Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   - Create a `.env` file in the root directory with your Google Cloud credentials:
     ```plaintext
     GOOGLE_APPLICATION_CREDENTIALS="path/to/your-google-credentials.json"
     ```
   
4. **Download Model Files** (Optional for Offline Models)
   - If you choose to use GPT-Neo or GPT-J locally, download the model weights from Hugging Face’s [EleutherAI models](https://huggingface.co/EleutherAI).

### Running the Project

To start the conversational interaction:
```bash
python main.py
```

Adjust the number of participants by modifying the `num_ais` parameter in `main.py` if you want more than two voices.

## Switching to a Paid API (e.g., OpenAI’s GPT-3)

To integrate a paid API instead of running offline models:
1. Replace the offline model pipeline in `helpers.py` with the OpenAI API call:
   ```python
   import openai

   def generate_response(last_message, max_retries=3):
       openai.api_key = "your-openai-api-key"
       response = openai.Completion.create(
           model="text-davinci-003",
           prompt=f"Respond to the following message naturally:\n\nMessage: {last_message}\nResponse:",
           max_tokens=50
       )
       return response.choices[0].text.strip()
   ```
2. Install the OpenAI Python package:
   ```bash
   pip install openai
   ```

3. Configure your API key as an environment variable or directly in the code.

This setup provides higher-quality responses and faster processing times compared to running models locally.

## Skills Demonstrated

This project showcases skills in:
- **Natural Language Processing (NLP)**: Implementing and fine-tuning language models for natural conversation generation.
- **API Integration**: Configuring APIs (e.g., Google Cloud, OpenAI) for speech recognition, synthesis, and text generation.
- **Python Programming**: Modular design, API calls, and real-time interaction.
- **Voice User Interface (VUI)**: Creating voice-based applications with distinct voices and smooth turn-based interactions.
- **Machine Learning Model Management**: Handling large models and exploring open-source vs. cloud-based solutions for NLP.

## Additional Notes

- **Performance Considerations**: Running GPT-J or GPT-Neo locally can be memory-intensive. A robust setup or cloud-based API (e.g., OpenAI’s GPT-3) may provide better performance.
- **Future Extensions**: Additional voices, alternative language models, or custom-trained models could be added to create more advanced AI interactions.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with any improvements or additional features.

---