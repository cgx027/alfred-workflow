''' remove http prefix and domain '''
from utils.input_output import get_single_user_input
from urllib.parse import urlparse

def run(query=''):
    link = get_single_user_input(query=query, index=1)
    output = urlparse(link)
    link_path = output.path
    print(link_path)
    return link_path

if __name__ == "__main__":
    run()