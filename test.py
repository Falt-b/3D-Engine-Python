import Engine.Object_Loader


def main():
    obj = Engine.Object_Loader.load_object("object.obj")
    print(f"{obj[0]} \n {obj[1]}")


if __name__ == "__main__":
    main()
