import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor

def main():
    pwd = __file__
    pwd_dir = pwd.rsplit("/", 1)[0]
    index_dir = os.path.join(pwd_dir, "index")
    index_file = os.path.join(index_dir, "index.json")

    if not os.path.exists(index_file):
        os.makedirs(index_dir, exist_ok=True)
        documents = SimpleDirectoryReader(os.path.join(pwd_dir, "data")).load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk(index_file)
    else:
        index = GPTSimpleVectorIndex.load_from_disk(index_file)
    while True:
        inp = input("聞きたいことを教えてください。\n>>>")
        print(index.query("日本語で答えてください。" + inp))
        print()


if __name__ == "__main__":
    main()