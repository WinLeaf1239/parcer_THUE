from general import Parcer

def main():
    parcer = Parcer(
        'https://5element.by/catalog/571-buterbrodnicy',
        'c-list__center',
    )

    try:
        parcer.accept_cookie()
        parcer.getlinks()
        parcer.creating_csv_file()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()