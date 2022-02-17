import os, logging

POINTER_SUFFIX = '.pointer'

logger = logging.getLogger(__name__)

# TODO: Add S3 support
def save(path, content_path, verbose=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        f.write(content_path)
    if verbose:
        logger.log(
            15,
            f'Saved pointer file to {str(path)} pointing to {str(content_path)}',
        )
