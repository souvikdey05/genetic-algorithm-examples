import argparse
import examples


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', '-e', type=str, default='Phrase_Generation',
                        choices=examples.__all__, help='Which example to run.')

    parser.add_argument('--config-file', '-f', type=str, 
                        required=True, help='Config file')

    parser.add_argument('--output-path', '-o', type=str, 
                        required=True, help='Path to save the monitoring log files.')

    options = parser.parse_args()

    ex_to_run = examples.__dict__[options.example]
    ex_to_run.main(options.config_file, options.output_path)


if __name__ == "__main__":
    main()