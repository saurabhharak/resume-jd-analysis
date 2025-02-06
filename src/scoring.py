import os
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from prompts import MATCH_ANALYSIS_PROMPT
def calculate_match_score_recommendations(candidate_info, jd_info, model="gpt-4o", temperature=0.2,):
    """
    Analyzes the match between candidate resume details and job description.

    Args:
        candidate_info (dict): Candidate resume details.
        jd_info (dict): Job description details.
        model (str, optional): OpenAI model to use. Defaults to "gpt-4o".
        temperature (float, optional): Sampling temperature for response generation. Defaults to 0.2.
        prompt_template (str, optional): Prompt template for the analysis.

    Returns:
        str: The analysis response from the LLM.
    """

    llm = ChatOpenAI(model=model, temperature=temperature)
    
    prompt = ChatPromptTemplate.from_template(MATCH_ANALYSIS_PROMPT)

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"resume_details": candidate_info, "job_description_details": jd_info})

    return response