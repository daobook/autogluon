import copy
import logging

logger = logging.getLogger(__name__)


def process_hyperparameters(hyperparameters: dict) -> dict:
    hyperparameters = copy.deepcopy(hyperparameters)

    top_level_keys = hyperparameters.keys()
    has_levels = any(
        isinstance(key, int) or key == 'default' for key in top_level_keys
    )

    if not has_levels:
        hyperparameters = {'default': hyperparameters}
    top_level_keys = hyperparameters.keys()
    for key in top_level_keys:
        for subkey in hyperparameters[key].keys():
            if not isinstance(hyperparameters[key][subkey], list):
                hyperparameters[key][subkey] = [hyperparameters[key][subkey]]
    if 'default' not in hyperparameters.keys():
        level_keys = [key for key in hyperparameters if isinstance(key, int)]
        max_level_key = max(level_keys)
        hyperparameters['default'] = copy.deepcopy(hyperparameters[max_level_key])
    return hyperparameters
