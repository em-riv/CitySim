

class Menu:

    def __init__(self, options):
        # { index: { "description" : Description, "function": func } }
        self.__options = options

    def __show_options(self):
        """
            Show all options from the menu
        """
        for key, value in self.__options.items():
            print(f"{key} - {value["description"]}")

    def __ask_input(self):
        """
            Ask the user an input, will validate the input and loop until have a good input
        :return: function associate to the menu item
        :rtype: function
        """
        entry = ""
        good_input = False
        while not good_input:
            try:
                entry = int(input(">"))
                if 0 > entry or entry > len(self.__options.keys()):
                    raise IndexError
            except ValueError:
                print("Please enter a number")
            except IndexError:
                print("Please enter a number between 1 and " + str(len(self.__options.keys())))
            else:
                good_input = True
        return self.__options[entry]["function"]

    def show(self):
        """
            show the menu, ask the input and launch the function associate
        """
        self.__show_options()
        func = self.__ask_input()
        func()

