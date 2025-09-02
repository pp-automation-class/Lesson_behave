import datetime
import logging
import random
import string
import time
import os


def element_exists(page, xpath: str, timeout: int = 0) -> bool:
    """Check if an element exists without throwing timeout errors.
    If timeout > 0, poll until timeout, otherwise check once.
    """
    if timeout and timeout > 0:
        end = time.time() + timeout / 1000
        while time.time() < end:
            if page.query_selector(xpath) is not None:
                return True
            page.wait_for_timeout(100)
        return False
    else:
        return page.query_selector(xpath) is not None


def log_files_path(name: str) -> str:
    log_dir = os.path.join("..", "..", "temp")
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, name)


def screenshot(page, name: str):
    screenshot_path = log_files_path(
        f"{name}{datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S%f')}.png"
    )
    page.screenshot(path=screenshot_path, full_page=True)
    logging.info(f"Screenshot saved to '{screenshot_path}'")


def random_username():
    return "".join(random.choice(string.ascii_letters) for _ in range(7))
