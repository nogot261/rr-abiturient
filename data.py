from dataclasses import dataclass


@dataclass(frozen=True)
class Applicant:
    full_name: str
    program: str
    score: int
    status: str


def build_demo_data() -> list[Applicant]:
    return [
        Applicant("Анна Петрова", "Прикладная информатика", 276, "Принято"),
        Applicant("Илья Смирнов", "Бизнес-информатика", 248, "На рассмотрении"),
        Applicant("Мария Волкова", "Прикладная информатика", 291, "Принято"),
    ]
