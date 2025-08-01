import logging
import os

class Logger:

    __instance = None

    def __new__(cls):
        """
            Singleton Pattern
        """
        if not cls.__instance:
            cls.__instance = super(Logger, cls).__new__(cls)
            cls.__instance.__initialisation()
        return cls.__instance

    def __initialisation(self):
        """
            Initialise our logger with all necessity parameters
        """
        self.__filename = "SimCityLogger.log"
        self.__logger = logging.getLogger("SimCityLogger")
        # set the minimum level our logger catch : DEBUG < INFO < WARNING < ERROR < CRITICAL
        # so with DEBUG it catch everything
        self.__logger.setLevel(logging.DEBUG)

        # The handler will catch the event and insert inside the file
        file_handler = logging.FileHandler(self.__filename, mode="a")
        file_handler.setLevel(logging.DEBUG)

        # Determine the format of the message
        formatter = logging.Formatter("Day %(day)s | %(levelname)s : %(message)s")

        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)

    def debug(self, day: int, message: str):
        self.__logger.debug(message, extra={"day": day})

    def info(self, day: int, message: str):
        self.__logger.info(message, extra={"day": day})

    def warning(self, day: int, message: str):
        self.__logger.warning(message, extra={"day": day})

    def error(self, day: int, message: str):
        self.__logger.error(message, extra={"day": day})

    def critical(self, day: int, message: str):
        self.__logger.critical(message, extra={"day": day})

    def get_log_day(self, day_log: int):
        logs = []
        try:
            with open(self.__filename, "r") as f:
                    for line in f.readlines():
                        day = line.split("|")[0].strip()[-1]
                        if int(day) == day_log:
                            logs.append(line)
        except FileNotFoundError:
            print("There is no logs")
        return logs

    def clear(self):
        """
            Clear all the logs ! Not use in production !
        """
        self.__logger.handlers.clear()
        os.remove(self.__filename)



if __name__ == "__main__":
    logger = Logger()
    logger.debug(0,"Beautifull day")
    logger.info(1,"A little cloudy day")
    logger.warning(2, "It's raining")
    logger.error(3,"A storm is raging")
    logger.critical(4, "A Tornado ! I'm homeless now")
    # logger.clear()
