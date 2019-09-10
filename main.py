import encoder
import decoder


def main():
    sel = int(input("encoder -> 1\ndecoder -> other\nselect : "))
    if sel == 1:
        encoder.encoder()
    else:
        decoder.decoder()


if __name__ == "__main__":
    main()
