from general import Parcer

def main():
    parcer = Parcer(
        'https://5element.by/catalog/571-buterbrodnicy',
        'c-list__center',
                
    )
    try:
        while True:
            parcer.getlinks()
            parcer.go_to_next_page()
    except:
        print('67')


if __name__ == '__main__':
    main()