import argparse
from genericpath import exists
import examples
import os
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', '-e', type=str, default='TSP',
                        choices=examples.__all__, help='Which example to run.')

    parser.add_argument('--config-file', '-f', type=str, 
                        required=True, help='Config file')

    parser.add_argument('--output-path', '-o', type=str, 
                        required=True, help='Path to save the monitoring log files.')

    options = parser.parse_args()

    base_path = os.getcwd()
    config_file = str(Path(base_path) / options.config_file)
    output_path = Path(base_path) / options.output_path
    output_path.mkdir(parents=True, exist_ok=True)
    output_path = str(output_path)

    ex_to_run = examples.__dict__[options.example]
    ex_to_run.main(config_file, output_path)


if __name__ == "__main__":
    main()