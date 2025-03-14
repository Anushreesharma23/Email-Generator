# Cold Email Generator Application

This Generative AI project simplifies the process of applying for jobs by generating tailored emails based on the content of job postings. With a simple link to the job opening, the application uses advanced AI technologies to create professional emails, saving users valuable time.

## Features
- **Automated Email Generation:** Input the link to a job posting, and the app generates a personalized email for the application.
- **Customizable for Personal Use:** Users can update their portfolio, resume links, and project details to ensure the email reflects their unique profile.
- **Powered by Cutting-Edge AI:** Utilizes LLaMA 3.1, LangChain, and GroqAPI for fast and accurate email generation.
- **Local Data Integration:** Incorporates personal data stored in `my_portfolio.csv` using ChromaDB.
- **Streamlit-based Interface:** Deployed as a user-friendly web application for easy accessibility.

**Deployed link:** [Email Generator App](https://anushreesharma23-email-generator-appmain-ber2tk.streamlit.app/)

---

## How to Use Locally
To run the application locally, follow these steps:

### 1. Clone the Repository
```bash
git clone <https://github.com/Anushreesharma23/Email-Generator/tree/main>
cd <App>
```
### 2. Install Dependencies
Ensure you have Python installed. Run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```
### 3. Start the Application
Navigate to the App directory and run the following command:

```bash
streamlit run .\App\main.py
```
## Customization Guide
This application allows users to tailor it for their specific needs, you can customise it:

### **Update Personal Data**
- Open the `my_portfolio.csv` file located in the resouces folder under App folder in the root directory.
- Add your **portfolio link**, **resume link**, and **project details**.

### **Modify Email Templates**
- Navigate to the `chains.py` file within the `App` directory.
- Update the **prompt template** in the file to customize how the LLM generates personalized emails based on the job posting.

---

## Dependencies
To ensure smooth operation, the following dependencies are required:

```plaintext
langchain==0.2.14
langchain_community==0.2.12
langchain_groq==0.1.9
unstructured==0.14.6
selenium==4.21.0
chromadb
streamlit
pysqlite3-binary
pandas==2.0.2
python-dotenv==1.0.0
```
## Tech Stack used
- **LLaMA 3.1**: For natural language generation.
- **LangChain**: To manage AI-powered workflows.
- **ChromaDB**: For personal data retrieval and integration.
- **GroqAPI**: Ensures faster and more efficient AI responses.
- **Streamlit**: Builds an interactive, user-friendly web interface.

**Feel Free to give more suggestion!**


