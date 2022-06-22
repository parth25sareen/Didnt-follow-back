print('-----------------------------------------------------')

class main:
    def __init__(self):

        self.__main()
        follow = []
        following = []
        imposter = []

    def __main(self):
        print(f"""
> Welcome to the imposter detection tool!
> This tool will detect if you are someone your following doesn't follow your back. \n
        """)
    
    def load_file(self, file_name):
        with open(file_name, "r") as f:
            list_ = f.readlines()
            return list_

    def write_file(self, imposter, list):
        with open(imposter, "w") as f:
            for items in list:
                f.write(items)

    def save_data(self, follow, following, imposter):
        follow = main.load_file(self, "follow.txt")
        following = main.load_file(self, "following.txt")
        imposter = main.load_file(self, "imposter.txt")

        for items in following:
            if items not in follow:
                imposter.append(items)


        main.write_file(self, 'imposter.txt', imposter)

        return f'> We have found {len(imposter)} imposter accounts.\n'

Main = main()

try: 

    follow = input('> Enter the name of the text file that contains the list of accounts you follow: ')
    following = input('> Enter the name of the text file that contains the list of accounts that follow you: ')   

except FileNotFoundError:
    print('> Error: File not found.')
    exit()

print(Main.save_data(follow, following, 'imposter.txt'))

print('> Created by: @parth25sareen at https://github.com/parth25sareen \n')

print('-----------------------------------------------------')

input('> Press enter to exit')