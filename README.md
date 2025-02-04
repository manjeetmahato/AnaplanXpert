
# AnaplanXpert - Multimodal RAG App

## Overview

**AnaplanXpert** is a cutting-edge multimodal Retrieval-Augmented Generation (RAG) application designed to assist Anaplan users. By combining advanced AI language generation with retrieval of relevant documentation and OCR capabilities, AnaplanXpert provides real-time, context-rich answers to queries related to Anaplan modeling, formulas, troubleshooting, and best practices.

## Key Features

- **Multimodal Input:**  
  Users can interact with the app via text and images. Upload images (such as screenshots or code snippets) to extract text using OCR for additional context.

- **Retrieval-Augmented Generation (RAG):**  
  The app integrates a language model with external search (via DuckDuckGo/Serper APIs) to retrieve and incorporate relevant documentation into the generated responses.

- **Real-Time Conversational Interface:**  
  Engage with a dynamic chat interface where questions and answers are presented with custom visual elements to distinguish between user and assistant responses.

- **Context Retention:**  
  The system maintains a short-term conversational memory to allow for follow-up questions and a more coherent dialogue.

- **Resource Integration:**  
  Links to official Anaplan resources—including the Anaplan website, help center, community forum, and product documentation—are provided in the sidebar for quick reference.

## How It Works

1. **Input & Query Processing:**  
   Users enter Anaplan-related queries via a chat interface. The app classifies the query (e.g., greeting, modeling question) and routes it accordingly.

2. **Documentation Retrieval:**  
   For queries involving "documentation" or "how to," the app searches official Anaplan resources and retrieves relevant information that is integrated into the final answer.

3. **Answer Generation:**  
   The language model (Google Gemini 1.5 Flash) generates detailed and context-specific responses by combining the retrieved documentation with the user's query.

4. **Multimodal Interaction:**  
   In addition to text, users can upload images to extract text content, enriching the query context and enabling a multimodal interaction.

## User Guide

### What Can You Do?

- **Ask Anaplan-Related Questions:**  
  Get help on writing formulas, configuring dashboards, or understanding modeling best practices.

- **Access Documentation:**  
  Use keywords like “documentation” or “how to” to retrieve detailed instructions from official Anaplan resources.

- **Upload Images:**  
  Provide screenshots or images containing text (such as error messages or code) to extract text and use it as context for your query.

### Interface Walkthrough

- **Sidebar:**  
  Contains useful links to Anaplan resources, an image uploader for OCR extraction, and a list of demo questions. Selecting a demo question will automatically send that query for you.

- **Main Chat Area:**  
  Displays a fixed title and chat history with custom icons representing both the user and the assistant. Your new queries are appended below previous messages so you can see the entire conversation history.

### Best Practices for Effective Queries

- **Include "Anaplan" When Applicable:**  
  Always mention “Anaplan” in your query if it relates to modeling, formulas, or dashboards to ensure the assistant understands the context.

- **Be Specific:**  
  Provide clear details, such as error messages, model names, or a description of the problem. For example, rather than asking "How do I filter data?" consider asking "How do I apply a dynamic filter to grid view 3 in Anaplan so it only shows data for Model 3?"

- **Utilize Demo Questions:**  
  If you’re unsure how to frame your query, select one of the demo questions from the sidebar. These examples are designed to help new users get started.

## Requirements & Setup

- **Python 3.x**
- **Streamlit** for the web interface
- **LangChain**, **DuckDuckGoSearchResults**, and **GoogleGenerativeAI** for AI and RAG functionalities
- **Tesseract OCR** and **Pillow** for image text extraction
- An `.env` file configured with your API keys (Google API, Serper API, etc.)

For detailed installation instructions, please refer to the [Installation](#installation) section in the project documentation.

## Limitations

- **Domain-Specific:**  
  The assistant is designed specifically for Anaplan-related queries.
- **Documentation Coverage:**  
  If relevant documentation is not available, the assistant will provide a fallback message.
- **Conversation History:**  
  The app retains only a limited history to maintain context for follow-up questions.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes. Feel free to open issues if you encounter any problems or have suggestions for new features.

## License

This project is licensed under the MIT License.

