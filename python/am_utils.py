import time


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
