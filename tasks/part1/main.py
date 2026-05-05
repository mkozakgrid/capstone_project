from task2 import set_to_dict

dict_to_update = {
    'a': 1,
    'b': 4,
    'c': 3
}

def main():
    set_to_dict(dict_to_update, a=0, b=4)

    print(dict_to_update)
  


if __name__ == "__main__":
    main()