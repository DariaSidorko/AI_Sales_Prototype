

import streamlit as st
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools.tavily_search import TavilySearchResults

from fpdf import FPDF

# Model and Agent tools
llm = ChatGroq(api_key=st.secrets.get("GROQ_API_KEY"))
search = TavilySearchResults(max_results=2)
parser = StrOutputParser()

# Custom CSS for modern UI
def apply_custom_css():
    st.markdown(
        """<style>
        .css-18e3th9 {
            padding: 2rem;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            font-size: 16px;
            border-radius: 5px;
            transition-duration: 0.4s;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .stTextInput input, .stTextArea textarea {
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        .sidebar-info {
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .footer {
            text-align: center;
            font-size: 0.9rem;
            margin-top: 2rem;
            color: #666;
            background-color: #f1f1f1;
            width: 100%;
            position: fixed;
            bottom: 0;
            left: 0;
            padding: 7px 0;
        }
        </style>""",
        unsafe_allow_html=True
    )

# Apply custom styles
apply_custom_css()

# Sidebar Information
with st.sidebar:
    st.markdown("""
    <div class="sidebar-info">
        <h3>About This App</h3>
        <p>Sales Assistant Agent helps sales representatives gather insights into prospective accounts, competitors, and company strategies.</p>
        <h4>Connect With Us</h4>
        <ul>
            <li><a href="https://www.linkedin.com" target="_blank">LinkedIn</a></li>
            <li><a href="https://www.twitter.com" target="_blank">Twitter</a></li>
            <li><a href="https://www.github.com" target="_blank">GitHub</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Page Header
st.title("Sales Assistant Agent")
st.markdown("Sales Assistant Agent Powered by Groq.")
st.markdown("### Generate insights into prospective accounts, competitors, and company strategies.")

# Function to generate PDF
def generate_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.splitlines():
        pdf.multi_cell(0, 10, line)
    return pdf

# Data collection/inputs
with st.form("sales_assistant", clear_on_submit=True):

    product_name = st.text_input("Product Name:", help="What is the product being sold?")
    company_url = st.text_input("Company URL:", help="Target company's website.")
    product_category = st.text_input("Product Category:", help="Category or domain of the product.")
    competitors = st.text_area("Competitors (URLs):", help="Enter competitor company URLs, separated by commas.")
    value_proposition = st.text_input("Value Proposition:", help="Short description of the product's value.")
    target_customer = st.text_input("Target Customer:", help="Name of the target individual or role.")

    # For the LLM insights result
    insights = ""

    # Data process
    if st.form_submit_button("Generate Insights"):
        if company_url:
            with st.spinner("Processing..."):

                # Search internet for company data
                company_data = search.invoke(company_url)

                # Format competitor URLs
                competitor_urls = competitors.split(',')
                competitor_data = [search.invoke(url.strip()) for url in competitor_urls]

                # Prompt
                prompt = f"""
                You are a sales assistant AI helping a sales rep. Analyze the following inputs to generate a one-page insight summary with the following sections:
                
                1. Company Strategy: Insights into the company's activities and priorities.
                2. Competitor Mentions: Mentions of competitors from input URLs or scraped data.
                3. Leadership Information: Relevant leaders and their roles.
                4. Product/Strategy Summary: Insights from public documents or reports.
                5. References: Links to articles, press releases, or other sources.
                
                Input Data:
                - Company Data: {{company_data}}
                - Competitor Data: {{competitor_data}}
                - Product Name: {{product_name}}
                - Product Category: {{product_category}}
                - Value Proposition: {{value_proposition}}
                - Target Customer: {{target_customer}}
                """

                # Prompt Template
                prompt_template = ChatPromptTemplate([("system", prompt)])

                # Chain
                chain = prompt_template | llm | parser

                # Result/Insights
                insights = chain.invoke({"company_data" : company_data, "competitor_data" : competitor_data, "product_name" : product_name, 
                                         "product_category" : product_category, "value_proposition" : value_proposition, "target_customer" : target_customer})

# Display Results
st.markdown("### Insights Summary")
st.markdown(insights)



# Download PDF
if insights:
    pdf = generate_pdf(insights)
    pdf_output = "sales_insights.pdf"
    pdf.output(pdf_output)
    with open(pdf_output, "rb") as pdf_file:
        st.download_button(
            label="Download Insights as PDF",
            data=pdf_file,
            file_name="sales_insights.pdf",
            mime="application/pdf"
        )


# Footer
st.markdown(
    """<div class="footer">
    &copy; 2024 Sales Assistant Agent. All rights reserved. Developed by DS.
    </div>""",
    unsafe_allow_html=True
)








