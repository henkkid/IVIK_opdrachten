class Print_options:

    def display_float_question(self, question):
        while True:
            try:
                awnser = float(input(question))
            except ValueError:
                print("Sorry, dat begreep ik niet, probeer het opnieuw")
                continue
            else:
                break

        return awnser

    def print_text(self, text):
        print(text)

    def print_result(self, party):
        if party.cake_count > 0:
            print(f"De taart die u kunt nemen is: {party.pie.name}")
            print(f"U heeft hiervoor {party.cake_count} cakes voor nodig")
            print(f"U houd {party.left_over_piecese} stukken over en {party.left_over_money} aan geld")
        else:
            print("er is geen taart voor u beschikbaar")
