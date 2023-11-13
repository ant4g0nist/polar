from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.embeddings import LocalAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings
from langchain.llms import Ollama


decompile_prompt = """\
This is a AI powered debugger working with a security engineer reverse engineering and malware analysis. You can decompile and provide pseudo C-code for the given disassembly ARM64, X86_64 architecuteres. Do not provide explanation for the decompiled pseudo code. Try and decompile as much as possible and bring to a higher level C-language.\

User: Hello, please decompile this {architecture} binary for me.\ Here's the disassembly: {disassembly}\
"""

disassembly_explanation_prompt = """\
This is a AI powered debugger working with a security engineer reverse engineering and malware analysis. You can decompile and provide pseudo C-code for the given disassembly ARM64, X86_64 architecuteres. Do not provide explanation for the decompiled pseudo code. Try and decompile as much as possible and bring to a higher level C-language.\

User: Hello, please explain this disassembly from a {architecture} binary for me. Here's the disassembly: {disassembly}\
"""

function_name_suggestion_prompt = """\
This is a AI powered debugger working with a security engineer reverse engineering and malware analysis. You can read the provided disassembly and suggest a highlevel function name that explains what the given disassembly does. This disassembly could be in ARM64, X86_64 architecuteres. Please provide a valid reason why you suggested the function name using atmost 100 words. \

User: Hello, please suggest a function name for disassembly from a {architecture} binary for me. Here's the disassembly: {disassembly}\
"""

def create_ai(ai, openai_api_key: str):
    if ai=="local":
        return LocalAIEmbeddings(
            openai_api_base="http://localhost:8080", model=localAiModel, openai_api_key=openai_api_key
            )
    elif ai=="ollama":
        return Ollama(model=ollamaModel)
    else:
        if openai_api_key:
            return ChatOpenAI(openai_api_base="http://localhost:3001", openai_api_key=openai_api_key)
        else:
            return LlamaCppEmbeddings(model_path="/Users/ant4g0nist/Desktop/Projects/LLM/llama-gpt/models/llama-2-7b-chat.bin")

def createDecompilePrompt(architecture: str, disassembly: str):
    prompt = PromptTemplate.from_template(decompile_prompt)
    return prompt.format(architecture=architecture, disassembly=disassembly)
    
def createDisassemblyExplanationPrompt(architecture: str, disassembly: str):
    prompt = PromptTemplate.from_template(disassembly_explanation_prompt)
    return prompt.format(architecture=architecture, disassembly=disassembly)

def createFunctionNameSuggestionPrompt(architecture: str, disassembly: str):
    prompt = PromptTemplate.from_template(function_name_suggestion_prompt)
    return prompt.format(architecture=architecture, disassembly=disassembly)

