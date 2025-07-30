from core.menu.menu import Menu


class MenuBuilder:
    """
        MenuBuilder is a utility class which will construct our object Menu by Builder Pattern
    """
    # { index: { "description" : Description, "function": func } }
    __options = {}

    @classmethod
    def add_option(cls, description, function):
        """

        :param description:
        :type description:
        :param function:
        :type function:
        :return:
        :rtype:
        """
        index = len(cls.__options.keys()) + 1
        cls.__options[index] = { "description" : description, "function" : function }
        return cls


    @classmethod
    def build(cls):
        menu = Menu(cls.__options)
        return menu

if __name__ == '__main__':

    menu = (MenuBuilder.add_option()
            .add_option()
            .build())