# User Guide: Anaplan Expert Assistant

Welcome to the **Anaplan Expert Assistant**! This interactive web app helps you troubleshoot, debug, and learn best practices for Anaplan modeling, formulas, dashboard filtering, and more—all powered by AI.

---

## Table of Contents

- [Getting Started](#getting-started)
- [How to Write Effective Queries](#how-to-write-effective-queries)
- [Troubleshooting & FAQs](#troubleshooting--faqs)
- [Final Notes](#final-notes)

---

## Getting Started

### Accessing the App
- **Launch the Application:** Open the web app in your browser using the provided URL (for example, `http://localhost:8501` when running locally or your deployed URL).
- **Interface Layout:**  
  - **Sidebar:** Contains links to Anaplan resources, a persistent image uploader, and branding.
  - **Main Chat Area:** Where you enter your queries and view responses from the assistant.

### Image Upload
- **Upload an Image:** Use the image uploader in the sidebar to upload a screenshot or photo of text (such as a dashboard, error message, or formula).
- **OCR Extraction:** The app uses Tesseract OCR to extract text from your image. The extracted text is then displayed and may provide context for your query.

### Chat Interface
- **Entering Your Query:** Type your question into the “Enter your Anaplan question:” field.
- **Receiving an Answer:** The assistant processes your query and displays the answer in the chat window. The final answer is also logged in the terminal.

---

## How to Write Effective Queries

### Best Practices
1. **Always Mention “Anaplan” When Relevant:**  
   Include the word **“Anaplan”** when your question relates to dashboards, formulas, or modeling issues.  
   *Example:* Instead of "How do I filter a grid view?" write "How do I filter a grid view in Anaplan?"

2. **Be Specific and Clear:**  
   Provide detailed information about your issue. Include model names, error messages, or code snippets if applicable.  
   *Example:* "My Anaplan dashboard’s grid view 3 shows data from Model 1 when filtered. How can I restrict it to show data only from Model 3?"

3. **Use Documentation Keywords for How-To Questions:**  
   If your query asks for instructions, include keywords like **“documentation”** or **“how to”**. This will trigger detailed, context-rich responses.

4. **For Debugging or Code Issues:**  
   Provide complete error messages or code snippets. Include “Anaplan” only if the issue directly relates to an Anaplan model or formula.

### Tips for Optimal Input
- **Review Your Query:** Ensure it is free of typos and clearly states the problem.
- **Context Matters:** Provide any relevant context about what you expect versus what is happening.
- **Multiple Queries:** The chat history retains up to the last 5 exchanges. Use previous context to build on your queries.

---

## Troubleshooting & FAQs

- **Unexpected or Incomplete Answers:**  
  Verify that your query includes “Anaplan” when necessary. If the response seems generic, rephrase your question with more details.

- **Image Upload Issues:**  
  Use high-quality images with clear, legible text for better OCR results.

- **Chat History:**  
  The app retains the last 5 interactions. If the conversation becomes too long, consider clearing the history to improve performance.

---

## Final Notes

- **For Code Debugging:**  
  You do not always need to include “Anaplan” unless the code snippet or error message directly involves an Anaplan model.
  
- **For Documentation Queries:**  
  Always include “documentation” or “how to” along with “Anaplan” for detailed responses.
  
- **Experiment and Explore:**  
  Try various queries and code snippets. Detailed inputs lead to more useful responses.

Enjoy using the Anaplan Expert Assistant!
