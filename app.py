from data import Applicant, build_demo_data


def accepted(applicants: list[Applicant], min_score: int = 260) -> list[Applicant]:
    return [item for item in applicants if item.score >= min_score]


def main() -> None:
    applicants = build_demo_data()
    print("Абитуриенты с баллом не ниже 260:")
    for item in accepted(applicants):
        print(f"{item.full_name}: {item.program}, {item.score}, {item.status}")


if __name__ == "__main__":
    main()
