from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

PLANNER_PROMPT = """You are an expert at analyzing research papers and creating a well structured plan for implementing the ideas in them.

TASK: Your task is to read the following research paper and create a plan for implementing the ideas in it.

Instructions:
1. Understand the research paper carefully.
2. Identify the key ideas and concepts presented in the paper.
3. Create a markdown text plan that outlines the steps needed to implement the ideas in the paper.
4. Break down complex ideas into smaller, manageable tasks.
5. Use clear and concise language to explain each step of the plan.
6. Organize the plan in a logical order, using headings and subheadings as necessary.
7. Include any relevant details, such as tools, technologies, or methodologies that should be used in the implementation.

RESEARCH PAPER TEXT:
{research_paper_text}
"""

planner_prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(PLANNER_PROMPT)
])