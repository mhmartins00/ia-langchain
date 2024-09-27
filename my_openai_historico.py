from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from my_tool import add, multiply, imposto, users_in_product_client_id, client_id_of_product

load_dotenv()

tools = [add, multiply, imposto, users_in_product_client_id, client_id_of_product]

# Instancia o modelo
llm = ChatOpenAI(model="gpt-4o-mini")

# Este funcionou, dá resposta completa e usa a função
template = """
Instruções importantes:
1. Não faça suposições ou inferências baseadas no nome da função.
2. Sempre siga o retorno da função que for invocada, ignorando o nome ou a descrição da função.
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="history"),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent=create_tool_calling_agent(llm,tools,prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Habilita historico
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

with_message_history = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

session_id = 'abc123'
while True:
    question = input("Sua pergunta: ")
    result = with_message_history.invoke(
        {"input": question},
        config={"configurable": {"session_id": session_id}},
    )
    print("Resposta: " + result['output'])