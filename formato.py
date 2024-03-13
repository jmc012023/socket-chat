class Formato:

    def __init__(self, figure: str) -> None:
        self.figure = figure
        self.COLORS = {
            "CYAN": "\033[36m",
            "RESET": "\033[0m"
        }

    def show_message(self, msm: str) -> None:
        length: int = len(msm)
        print(f"\t{self.COLORS['CYAN']}{self.figure * (length + 4)}{self.COLORS['RESET']}")
        print(f"\t{self.COLORS['CYAN']}{self.figure}{self.COLORS['RESET']}" + " " * (length + 2) + f"{self.COLORS['CYAN']}{self.figure}{self.COLORS['RESET']}")
        print(f"\t{self.COLORS['CYAN']}{self.figure}{self.COLORS['RESET']} {msm} {self.COLORS['CYAN']}{self.figure}{self.COLORS['RESET']}")
        print(f"\t{self.COLORS['CYAN']}{self.figure}{self.COLORS['RESET']}" + " " * (length + 2) + f"{self.COLORS['CYAN']}{self.figure}{self.COLORS['RESET']}")
        print(f"\t{self.COLORS['CYAN']}{self.figure * (length + 4)}{self.COLORS['RESET']}")