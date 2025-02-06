from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.chains import LLMChain
from prompts import JD_EXTRACTION_PROMPT, RESUME_EXTRACTION_PROMPT
import os
import sys
from langchain_openai import ChatOpenAI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import OPENAI_API_KEY



def process_job_description(job_description, model_name="gpt-4o-mini", temperature=0):
    schemas = [
        ResponseSchema(name="Job Title", description="A python list The title of the job."),
        ResponseSchema(name="skills", description="A python list of required skills."),
        ResponseSchema(name="experience_years", description="A python list of Number of years of required experience (an integer)."),
        ResponseSchema(name="certifications", description="A python list of certifications required."),
        ResponseSchema(name="education", description="A python list of educational Qualifications."),
        ResponseSchema(name="other", description="A python list of Any additional requirements or qualities.")
    ]

    output_parser = StructuredOutputParser.from_response_schemas(schemas)

    format_instructions = output_parser.get_format_instructions()

    prompt = PromptTemplate(
        template=JD_EXTRACTION_PROMPT,
        input_variables=["job_description"],
        partial_variables={"format_instructions": format_instructions}
    )


    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    chain = LLMChain(llm=llm, prompt=prompt)

    raw_response = chain.run(job_description=job_description)

    extracted_info = output_parser.parse(raw_response)

    return extracted_info

def extract_resume_info(resume_text: str, model_name: str = "gpt-4o-mini", temperature: float = 0):
    """
    Extracts structured information from a resume using OpenAI's language model.
    
    :param resume_text: The text content of the candidate's resume.
    :param model_name: The OpenAI model to use (default: "gpt-4o-mini").
    :param temperature: The model's temperature setting (default: 0 for deterministic responses).
    :return: A dictionary containing extracted resume details.
    """
    schemas = [
        ResponseSchema(name="Candidate", description="A python list the candidate's Name"),
        ResponseSchema(name="Job Title", description="A python list The title of the job."),
        ResponseSchema(name="skills", description="A python list of required skills."),
        ResponseSchema(name="experience_years", description="A python list of Number of years of required experience (an integer)."),
        ResponseSchema(name="certifications", description="A python list of certifications required."),
        ResponseSchema(name="education", description="A python list of educational Qualifications."),
        ResponseSchema(name="other", description="A python list of Any additional requirements or qualities.")
    ]
    
    output_parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = output_parser.get_format_instructions()
    
    
    prompt = PromptTemplate(
        template=RESUME_EXTRACTION_PROMPT,
        input_variables=["resume_text"],
        partial_variables={"format_instructions": format_instructions}
    )
    
    llm = ChatOpenAI(model_name=model_name, temperature=temperature)
    chain = LLMChain(llm=llm, prompt=prompt)
    
    raw_response = chain.run(resume_text=resume_text)
    extracted_info = output_parser.parse(raw_response)
    
    return extracted_info