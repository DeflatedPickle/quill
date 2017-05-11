from quill import Window


class Calculator(Window):
    def startup(self):
        self.menu()

    def menu(self, *args):
        self.enable()
        self.clear()

        self.insert_text("Calculator", True, tag="Heading-4")
        self.insert_text("What calculation would you like to do?", True)

        self.insert_command("> Addition", command=lambda *args: self.calculate(calculation="add"))
        self.insert_command("> Subtraction", command=lambda *args: self.calculate(calculation="subtract"))
        self.insert_command("> Multiplication", command=lambda *args: self.calculate(calculation="multiply"))
        self.insert_command("> Division", command=lambda *args: self.calculate(calculation="divide"))

        self.goto_end()
        self.disable()

    def calculate(self, calculation: str="", *args):
        self.enable()
        self.clear()

        method = "+" if calculation == "add" else "-" if calculation == "subtract" else "*" if calculation == "multiply" else "/" if calculation == "divide" else ""

        self.insert_text("What numbers would you like to {}?".format("add" if calculation == "add" else "subtract" if calculation == "subtract" else "multiply" if calculation == "multiply" else "divide" if calculation == "divide" else ""), True)
        first_number = self.insert_ttk_entry()
        self.insert_text(" {} ".format(method))
        second_number = self.insert_ttk_entry()
        self.insert_new_line()
        self.insert_command("Calculate", command=lambda *args: self.work_out(int(first_number.get()), int(second_number.get()), method))
        self.insert_command("< Back", command=self.menu)

        self.goto_end()
        self.disable()

    def work_out(self, first: int=0, second: int=0, calculation: str="", *args):
        self.enable()

        answer = None
        if calculation == "+":
            answer = first + second
        elif calculation == "-":
            answer = first - second
        elif calculation == "*":
            answer = first * second
        elif calculation == "/":
            answer = first / second

        self.insert_text(str(answer), True, "end-8c")

        self.goto_end()
        self.disable()


def main():
    app = Calculator(title="Calculator")
    app.mainloop()


if __name__ == "__main__":
    main()
