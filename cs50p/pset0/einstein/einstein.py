SPEED_OF_LIGHT = 299792458  # metres per second


def einstein(mass):
    """Return the energy in joules for a mass in kilograms (E = mc^2)."""
    return mass * SPEED_OF_LIGHT ** 2


def main():
    mass = int(input("Mass in kilograms: "))
    print(einstein(mass))


if __name__ == "__main__":
    main()