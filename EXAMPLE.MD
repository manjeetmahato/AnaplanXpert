# Example Questions & Code Samples for Anaplan Expert Assistant

This file contains demo questions and complex code examples designed to help new users get started with the Anaplan Expert Assistant. Use these examples as a guide when formulating your own queries.

---

## Demo Questions

1. **Basic Anaplan Query:**  
   - **Question:**  
     "How do I create a dynamic filter in Anaplan?"  
   - **Tip:** Make sure to include "Anaplan" so the assistant understands the context.

2. **Dashboard Filtering Issue:**  
   - **Question:**  
     "In my Anaplan dashboard, grid view 3 shows data from Model 1 when filtered. How do I ensure grid view 3 displays data only for Model 3?"

3. **Formula Debugging:**  
   - **Question:**  
     "I am receiving an 'Invalid reference' error in my Anaplan model at cell A12. What are some common causes of this error?"

4. **Documentation-Based Query:**  
   - **Question:**  
     "How to configure documentation-based filters in Anaplan? Please provide detailed instructions."  
   - **Tip:** Including keywords like "documentation" or "how to" triggers the assistant to provide more detailed, context-rich answers.

---

## Complex Code Examples

### Example 1: Anaplan Formula Issue
**Scenario:**  
You have a formula that should calculate adjusted sales, but sometimes it returns an error.

**Code Snippet:**
```plaintext
IF Line Item 1 = "Active" THEN 
    Sales * (1 + Growth Rate) 
ELSE 
    Sales 
ENDIF
