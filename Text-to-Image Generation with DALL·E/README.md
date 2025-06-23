# Text-to-Image Generation with OpenAI DALL·E

This project demonstrates how to generate high-quality, stylized images from text using OpenAI's DALL·E-3 API. It also introduces prompt engineering techniques to creatively control and improve generated outputs.

## Overview

The notebook guides users through:
- **Basic Image Generation** from text prompts
- Applying **Style Modifiers** (e.g., “rendered in Unity” or “made of glass”)
- Using **Quality Boosters** (e.g., “4K”, “high resolution”, “masterpiece”)
- Applying **Repetition** to emphasize or exaggerate features in the output

> Example:  
> Prompt - `"A very very very beautiful pyramid in 4K, made of crystal"`  
> Result - [Image auto-displayed inside the notebook]

---

## Tech Stack

- **Python 3.x**
- **OpenAI Python SDK**
- **Jupyter Notebook / IPython**
- `getpass` for API key security

## Installation

To run locally:

```bash
pip install openai ipython getpass



How to Use
Clone this repository.

Open the notebook in Jupyter.

Run the first cell to input your OpenAI API key securely.

Customize your prompts and run the generation code.
Use Case
This project can be used in:

Marketing campaigns for visual concept testing

Creative content generation for articles or blogs

Rapid visual prototyping in product design

Educational demonstrations of Generative AI

Output
Each cell generates and displays an image using IPython.display.Image and OpenAI’s hosted image URL.

Note on API Usage
Make sure you have an OpenAI API key. You can get one at https://platform.openai.com/account/api-keys.
