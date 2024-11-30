import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    # Set the page configuration
    st.set_page_config(
        layout="wide",
        page_title="Cold Mail Generator",
        page_icon="📧"

    )

    # Apply custom styles
    st.markdown(
        """
        <style>
        /* General Styling */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #000000;
        }

        /* Title Styling */
        .main-title {
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            color: #000000;
        }

        .sub-title {
            text-align: center;
            font-size: 1.3em;
            color: #4B5563;
        }

        /* Container Styling */
        .stButton > button {
            background-color: #4B6A9B;
            color: white;
            font-size: 1em;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #354D73;
        }

        .footer {
            text-align: center;
            font-size: 0.9em;
            margin-top: 50px;
            color: #9CA3AF;
        }

        .expander > div > div {
            background-color: #E5E7EB;
            border-radius: 8px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add a header section
    st.markdown(
        """
        <div>
            <p class="main-title">📧 Cold Mail Generator</p>
            <p class="sub-title">Generate professional emails tailored to job postings in just a few clicks!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Create a container for the input form
    with st.container():
        st.markdown("### Step 1: Provide the Job URL")
        url_input = st.text_input(
            "Enter the career page or job URL below:",
            value="https://impetus.openings.co/#!/job-view/ai-ml-engineer-2024080110424691",
            help="Paste the link to the job posting or career page.",
        )
        submit_button = st.button("Fetch Job Details")

    # Display results after fetching
    if submit_button:
        with st.container():
            st.markdown("### Step 2: Job Details & Generated Email")
            try:
                # Process the input URL
                with st.spinner("Extracting job details and generating the email..."):
                    loader = WebBaseLoader([url_input])
                    data = clean_text(loader.load().pop().page_content)
                    portfolio.load_portfolio()
                    jobs = llm.extract_jobs(data)

                # Display job details and email generation
                for idx, job in enumerate(jobs, start=1):
                    with st.expander(f"Job #{idx}: {job.get('role', 'Unknown Role')}"):
                        st.write(f"**Role**: {job.get('role', 'N/A')}")
                        st.write(f"**Experience**: {job.get('experience', 'N/A')}")
                        st.write(f"**Skills**: {', '.join(job.get('skills', []))}")
                        st.write(f"**Description**: {job.get('description', 'N/A')}")

                        # Fetch related portfolio links and generate the email
                        skills = job.get('skills', [])
                        links = portfolio.query_links(skills)
                        email = llm.write_mail(job, links)

                        # Display the generated email
                        st.markdown("#### Generated Email:")
                        st.code(email, language='markdown')

            except Exception as e:
                st.error(f"An Error Occurred: {e}")

    # Add a footer
    st.markdown(
        """
        <div class="footer">
            Made with ❤️ using Streamlit | Powered by LangChain
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)
