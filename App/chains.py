import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
    
            ### INSTRUCTION:
            Write a **One professional email** tailored to the recruiter for the given job opening.
            You are Anushree Sharma, a final-year BTech student at Madhav Institute of Technology and Science, specializing in Computer Science and Design, 
            with a CGPA of 8.73/10. You have gained valuable experience through internships in data science and software development, 
            where you contributed to impactful projects such as a Knowledge Retrieval System using LLaMA 2 and Retrieval-Augmented Generation (RAG) 
            and a Digital Signature Application leveraging React.js. You possess strong skills in Python, machine learning, full-stack development, and AI.
            Write a professional email to the recruiter for the mentioned job opening, emphasizing:
            - How your skills and projects align with the job requirements.
            - Your passion for problem-solving and innovative solutions.
            - Your ability to contribute to the company's success through your technical expertise and adaptability.
            Also add the most relevant ones from the following links to your portfolio: {link_list}
            Additionally, highlight any relevant technologies you've worked with, such as LLaMA 2, RAG, TensorFlow, React.js, and cloud platforms. 
            Ensure the email is concise, enthusiastic, and tailored to the role.
            At the end do not forgot to mention your phone no. which is 9109837107 and your email which is anushreesharma232003@gmail.com.
            ### EMAIL (NO PREAMBLE):
    
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))