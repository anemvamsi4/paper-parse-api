from langchain.chat_models.base import BaseChatModel

from .prompts import planner_prompt
from .markdown_extraction import get_markdown

def generate_plan(pdf_path: str, llm: BaseChatModel) -> str:
    """
    Generate a plan for implementing ideas from a research paper in PDF format using the Datalab API and LLM.
    
    Args:
        pdf_path (str): Path to the PDF file to process.
        llm (BaseChatModel): The language model to use for generating the plan.
        
    Returns:
        str: The generated plan in markdown format.
    """
    # Step 1: Extract text from the PDF using Datalab API
    research_paper_text = get_markdown(pdf_path)['markdown']

    # Step 2: Format the prompt with inputs
    prompt = planner_prompt.format_messages(
        research_paper_text=research_paper_text
    )

    # Step 3: Generate the plan using the LLM
    response = llm.invoke(prompt)

    return response.content
