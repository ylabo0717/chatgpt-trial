import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor

def main():
    pwd = __file__
    pwd_dir = pwd.rsplit("/", 1)[0]
    index_dir = os.path.join(pwd_dir, "index")
    index_file = os.path.join(index_dir, "index.json")

    if not os.path.exists(index_file):
        os.makedirs(index_dir, exist_ok=True)
        documents = SimpleDirectoryReader(os.path.join(pwd_dir, "data")).load_data()
        index = GPTVectorStoreIndex.from_documents(documents)
        index.storage_context.persist()
    else:
        index = GPTVectorStoreIndex.load_from_disk(index_file)

    query_engine = index.as_query_engine()
    while True:
        val = input("質問を入力してください \n>>>")
        if val == 'q':
            print('FINISH')
            break
        else:
            print(query_engine.query("日本語で答えてください。" + val))
            print()

if __name__ == "__main__":
    main()

