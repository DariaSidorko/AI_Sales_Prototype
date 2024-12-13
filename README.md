
# Sales Assistant Agent Prototype LIVE link

https://salesagentprototype.streamlit.app

# Sales Assistant Agent Prototype

Welcome to the Sales Assistant Agent application! This tool is designed to help sales representatives generate actionable insights into prospective accounts, competitors, and company strategies. Below, you will find a detailed overview of the system, its usage, and technical structure.

---

## Features
- **Company Insights**: Analyze company activities and priorities.
- **Competitor Analysis**: Retrieve and summarize competitor data.
- **Leadership Information**: Gather information about relevant company leaders.
- **Customizable PDF Reports**: Generate and download insights in a professional format.

---

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Required Python libraries:
  - `streamlit`
  - `langchain`
  - `fpdf`
  - `tavily-search`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sales-assistant-agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sales-assistant-agent
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up API keys in the `.streamlit/secrets.toml` file:
   ```toml
   [groq_api]
   GROQ_API_KEY = "your_api_key_here"
   ```

### Running the Application
Start the Streamlit app:
```bash
streamlit run app.py
```
Open your browser and navigate to the provided localhost URL.

---

## Usage
1. **Input Details**:
   - Fill out the form with details such as product name, company URL, competitors, and target customer.
2. **Generate Insights**:
   - Click the "Generate Insights" button. The app will retrieve and analyze relevant data.
3. **View Results**:
   - Insights will be displayed on the main page.
4. **Download PDF**:
   - Download the generated insights as a professionally formatted PDF.

---

## Technical Overview

### Code Structure

#### 1. Overview
The Sales Assistant Agent application is built using the following technologies:
- **Streamlit**: Provides an interactive web interface.
- **LangChain**: Powers the AI-based reasoning and prompt processing using ChatGroq.
- **TavilySearchResults**: Retrieves relevant information from the web.
- **FPDF**: Converts generated insights into downloadable PDF documents.

#### 2. Components

**a. User Interface (UI)**
- **Custom CSS**: Enhances the application’s appearance and usability.
- **Sidebar**: Displays app information and links to social media platforms.
- **Input Form**: Collects user inputs such as Product Name, Company URL, Competitors, etc.

**b. Backend Logic**
- **Input Collection**: Collects details such as product name, company URL, and competitors for processing.
- **Data Retrieval**: Uses TavilySearchResults to fetch relevant information from provided URLs.
- **AI Insights Generation**: Leverages LangChain with structured prompts to produce concise insights using ChatGroq.
- **PDF Export**: Formats and exports insights into a shareable PDF document using FPDF.

**c. Workflow**
1. Users submit details through a form.
2. TavilySearchResults fetches company and competitor data.
3. LangChain processes inputs using a predefined prompt to generate structured insights.
4. Insights are displayed and offered as a downloadable PDF.

---

## Time Management

| Task                  | Time Allocated | Explanation                                           |
|-----------------------|----------------|-------------------------------------------------------|
| Research and Planning | 2 hours        | Analyzed requirements and identified tools.           |
| Environment Setup     | 1 hour         | Configured Streamlit, LangChain, and TavilySearch.    |
| UI Development        | 2 hours        | Created user inputs, layout, and styling.             |
| Backend Implementation| 3 hours        | Integrated AI, data retrieval, and PDF generation.    |
| Testing and Debugging | 2 hours        | Validated functionality and resolved issues.          |
| Documentation         | 1.5 hours      | Documented technical details and workflow.            |

---

## Challenges and Solutions

### Challenge 1: Invalid URLs or No Data
**Problem**: Some user-provided URLs were invalid or returned no results.
**Solution**: Implemented validation checks for URLs and provided user-friendly error messages when no data was retrieved.

### Challenge 2: Long Processing Time
**Problem**: Fetching data for multiple competitors caused delays.
**Solution**: Restricted the number of competitor URLs and optimized processing using batch queries where possible.

---

## Experiments

### Prompt Engineering
**Objective**: Refined prompts to improve the quality of generated insights.
**Outcome**: Including distinct sections like Company Strategy and Leadership Information enhanced clarity and relevance.

### Search Tuning
**Objective**: Adjusted the maximum results parameter in TavilySearchResults.
**Outcome**: Limiting results to 2 provided concise and relevant data.

### Model Comparisons
**Objective**: Compared ChatGroq with other language models.
**Outcome**: ChatGroq delivered consistent and high-quality insights for this use case.

---

## System Outputs

### Example One-Pager

**Company Strategy**: The target company is focused on digital transformation and expanding into emerging markets. Recent initiatives include AI-driven customer service enhancements.

**Competitor Mentions**:
- **Competitor A**: Known for its robust supply chain integration.
- **Competitor B**: Focuses heavily on sustainable product development.

**Leadership Information**:
- **John Doe, CEO**: Drives innovation and expansion strategies.
- **Jane Smith, CTO**: Leads technical teams for AI adoption.

**Product/Strategy Summary**: The product aligns with the company’s goal of increasing operational efficiency through automation.

---

## Future Improvements

- Enhance data retrieval capabilities by integrating advanced search APIs.
- Add multilingual support for a broader user base.
- Improve PDF formatting with visual elements like charts or infographics.
- Implement asynchronous data fetching for better performance with large datasets.

---

## Contributions
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push the changes:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## Contact
For any questions or feedback, feel free to reach out to:
- Email: support@salesassistantagent.com
- LinkedIn: [Sales Assistant Agent](https://www.linkedin.com)
- GitHub: [Repository](https://github.com/your-repo/sales-assistant-agent)

---

**Happy Selling!** 🚀

---
