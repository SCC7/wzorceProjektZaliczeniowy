from urzadzenie import Urzadzenie


class Ekspres:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> None:
        return self._builder

    @builder.setter
    def builder(self, urzadzenie: Urzadzenie) -> None:
        self._builder = urzadzenie

    def build_minimal_version(self) -> None:
        self.builder.produce_part_a()

    def build_full_version(self) -> None:
        self.builder.wypelnianie()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
