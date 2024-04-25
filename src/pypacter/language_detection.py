"""
Programming language detection
"""

from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from pypacter import models


def detect_language(code_snippet):
    """
    Detect the most likely programming language of a given code snippet.

    Args:
        code_snippet (str): The code snippet to analyze.

    Returns:
        str: The detected programming language.
    """

    template = """you are a programming language interpreter and
    return only programming language name for '{code_snippet}' code snippet."""

    prompt = PromptTemplate(
        input_variables=["code_snippet"],
        template=template
        )
    chain = LLMChain(llm=models.DEFAULT_MODEL, prompt=prompt)
    output = chain.run({"code_snippet": code_snippet})
    return str(output["text"]).lower()
