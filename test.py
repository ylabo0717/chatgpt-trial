import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import StorageContext, load_index_from_storage


def check_files_exists(file_path_list):
    for file_path in file_path_list:
        if not os.path.exists(file_path):
            return False
    return True


def main():
    pwd = __file__
    pwd_dir = pwd.rsplit("/", 1)[0]
    storage_dir = os.path.join(pwd_dir, "storage")
    index_file_list = [os.path.join(storage_dir, "docstore.json"), os.path.join(
        storage_dir, "index_store.json"), os.path.join(storage_dir, "vector_store.json")]

    if check_files_exists(index_file_list):
        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
        # load index
        index = load_index_from_storage(storage_context)
    else:
        documents = SimpleDirectoryReader(
            os.path.join(pwd_dir, "data")).load_data()
        index = GPTVectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=storage_dir)

    query_engine = index.as_query_engine()

    while True:
        val = input("質問を入力してください \n>>>")
        if val == 'q':
            print('終了します')
            break
        else:
            print(query_engine.query("日本語で答えてください。" + val))
            print()


if __name__ == "__main__":
    main()
