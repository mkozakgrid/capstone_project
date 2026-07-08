import argparse
import json
from faker import Faker

fake = Faker()


def generate_dicts(number: int, fields: dict[str, str]) -> list[dict]:
    result = []
    for _ in range(number):
        record = {}
        for field, provider in fields.items():
            generator = getattr(fake, provider, None)
            if generator is None or not callable(generator):
                raise ValueError(f"Unknown Faker provider: '{provider}'")
            record[field] = generator()
        result.append(record)
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Generate fake data dicts using Faker providers.",
        usage="%(prog)s NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER ...]",
    )
    parser.add_argument("number", type=int, help="Number of dicts to generate")

    args, remaining = parser.parse_known_args()

    if args.number <= 0:
        parser.error("NUMBER must be a positive integer")

    fields = {}
    for arg in remaining:
        if not arg.startswith("--") or "=" not in arg:
            parser.error(f"Named arguments must be in the format --FIELD=PROVIDER, got: {arg}")
        key, _, value = arg[2:].partition("=")
        if not key or not value:
            parser.error(f"Invalid argument: {arg}")
        fields[key] = value

    if not fields:
        parser.error("At least one --FIELD=PROVIDER argument is required")

    records = generate_dicts(args.number, fields)
    for record in records:
        print(json.dumps(record))


if __name__ == "__main__":
    main()
