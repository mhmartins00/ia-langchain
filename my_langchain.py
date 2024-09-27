from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from math_tool import multiply, add

load_dotenv()

tools = [add, multiply]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente de IA altamente especializado em resolver cálculos e tarefas baseadas no retorno de ferramentas externas."),
        ("system", """
        Instruções importantes:
        1. Sempre siga *exclusivamente* o retorno da função que for invocada, ignorando o nome ou a descrição da função.
        2. Não faça suposições ou inferências baseadas no nome da função; apenas use o resultado fornecido como a resposta final.
        3. Quando uma função for chamada, seu único objetivo é processar e retornar o valor exato que a função fornecer.
        4. Se o valor retornado não corresponder às expectativas lógicas (por exemplo, por erro da ferramenta), ainda assim, deve ser retornado exatamente o que foi fornecido pela função.
        5. Não realize cálculos, ajustes ou explicações adicionais por conta própria; a função e o retorno dela são a única verdade.
        """),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

llm = ChatOpenAI(model="gpt-4o-mini")

agent=create_tool_calling_agent(llm,tools,prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# result = agent_executor.invoke({"input": "Quanto é 4 + 6:"})
# result = agent_executor.invoke({"input": "Quanto é 4 + 6:"})

# print(result)

def executeQuestion(query: str):
    return agent_executor.invoke({"input": query})