from api import get_crypto_data
from writefile import write_file

def main():

    data = get_crypto_data()
    write_file(str(data))

if __name__ == "__main__":
    main()