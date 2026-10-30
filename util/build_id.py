import os
import random


def main():
    # VIAL_BUILD_ID pins the ID for reproducible builds; otherwise pick a random one.
    if "VIAL_BUILD_ID" in os.environ:
        build_id = int(os.environ["VIAL_BUILD_ID"], 0)
    else:
        build_id = random.randrange(0, 2 ** 24 - 1)
    print("#define BUILD_ID ((uint32_t)0x{:08X})".format(build_id))


if __name__ == "__main__":
    main()
