# Representa um unico commit no historico de versoes.
class Commit:
    # O construtor inicializa os dados do commit.
    # O pai e opcional porque o primeiro commit do projeto nao tem pai.
    def __init__(self, identificador, mensagem, autor, pai=None):
        self.id = identificador
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    # Imprime os dados deste commit e chama recursivamente o commit pai.
    def historico(self):
        print(f"#{self.id} {self.mensagem} ({self.autor})")

        # Caso base: se nao tiver pai, encerramos a recursao sem usar else
        if self.pai is None:
            return

        self.pai.historico()
