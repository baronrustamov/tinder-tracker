import pynder


def find(XAuthToken, user_id, lon, lat):
    session = pynder.Session(XAuthToken=XAuthToken)
    session.update_location(lat, lon)
    print("starting to search...")

    users = session.nearby_users()

    for user in users:
        if user.id == user_id:
            print("current pos: " + str(session.profile.pos))
            print("distance to " + user.name + " = " + str(user.distance_km))


def main():
    XAuthToken = 'your token'

    lon = 0
    lat = 0
    id_to_track = 'id to track...'

    find(XAuthToken=XAuthToken, user_id=id_to_track, lon=lon, lat=lat)


if __name__ == "__main__":
    main()
