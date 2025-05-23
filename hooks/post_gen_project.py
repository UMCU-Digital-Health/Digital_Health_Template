"""Script to run after the project is generated."""

import shutil
import logging
import subprocess

logger = logging.getLogger(__name__)

def setup_uv():
    """Setup environment using uv and install nbstripout"""

    # If uv is not installed return an error message and abort
    if shutil.which("uv") is None:
        logger.error("uv is not installed. Please install it first.")
        raise SystemExit(1)

    logger.info("Setting up git...")
    subprocess.run(["git", "init"], check=True)

    logger.info("Setting up uv and installing nbstripout...")
    subprocess.run(["uv", "sync"], check=True)
    subprocess.run(["uv", "run", "nbstripout", "--install"], check=True)
    logger.info("Setup complete")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    setup_uv()