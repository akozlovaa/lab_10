from model.tour import Tour


def main():
    italy = Tour("Italy", 14, 21000, 4, "Grand Hotel", "plane")
    greece = Tour("Greece", 7, 15000, 25, "Leopolis", "bus")
    cyprus = Tour("Cyprus", 16, 35000, 18, "George", "train")
    print(italy.__str__())
    print(greece.__str__())
    print(cyprus.__str__())


if __name__ == "__main__":
    main()
