import pynder


def find(XAuthToken, lon, lat):
    session = pynder.Session(XAuthToken=XAuthToken)
    session.update_location(lat, lon)
    print("starting to search...")

    users = session.nearby_users()

    for user in users:
        if user.name == 'name to search' and user.age == 100:
            print(user.name + ", " + str(user.age) + ", " + str(user.id))
            for photo in user.get_photos():
                print(photo)


def main():
    XAuthToken = 'your token'

    lon = 14.123425
    lat = 46.616233

    find(XAuthToken=XAuthToken, lon=lon, lat=lat)


if __name__ == "__main__":
    main()
