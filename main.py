import argparse
import examples


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', '-e', type=str, default='Phrase_Generation',
                        choices=examples.__all__, help='Which example to run.')

    parser.add_argument('--config-file', '-f', type=str, 
                        required=True, help='Config file')

    options = parser.parse_args()

    ex_to_run = examples.__dict__[options.example]
    ex_to_run.main(options.config_file)


if __name__ == "__main__":
    main()