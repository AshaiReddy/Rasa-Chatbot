import argparse
import logging

from rasa.shared.constants import DEFAULT_RESULTS_PATH
from rasa.test import perform_nlu_cross_validation, test_nlu

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")


DEFAULT_DATA_PATH = "data"
DEFAULT_MODELS_PATH =  "models"

def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        required=True,
        help="DEFAULT - for basic NLU model test. VALIDATION - for NLU cross validation",
    )

    return parser


def test_nlu_model():
    nlu_data = DEFAULT_DATA_PATH + "/nlu"
    test_nlu(DEFAULT_MODELS_PATH, nlu_data,DEFAULT_RESULTS_PATH,{})

def test_nlu_model_cross_validation() -> None:
    nlu_data = DEFAULT_DATA_PATH + "/nlu"
    perform_nlu_cross_validation('config.yml', nlu_data, DEFAULT_RESULTS_PATH,{})

if __name__ == "__main__":
    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()
    test_type = cmdline_arguments.type

    if test_type == "DEFAULT":
        test_nlu_model()
    elif test_type == "VALIDATION":
        test_nlu_model_cross_validation()
    else:
        logger.info("please provide a valid option")
