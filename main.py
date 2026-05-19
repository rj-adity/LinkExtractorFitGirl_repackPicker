import os
import re
import requests

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)


# ==========================================
# CONSOLE CLASS
# ==========================================

class console:

    def __init__(self):

        self.colors = {
            "green": Fore.GREEN,
            "red": Fore.RED,
            "yellow": Fore.YELLOW,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE,
            "black": Fore.BLACK,
            "reset": Style.RESET_ALL,
            "lightblack": Fore.LIGHTBLACK_EX,
            "lightred": Fore.LIGHTRED_EX,
            "lightgreen": Fore.LIGHTGREEN_EX,
            "lightyellow": Fore.LIGHTYELLOW_EX,
            "lightblue": Fore.LIGHTBLUE_EX,
            "lightmagenta": Fore.LIGHTMAGENTA_EX,
            "lightcyan": Fore.LIGHTCYAN_EX,
            "lightwhite": Fore.LIGHTWHITE_EX
        }

    def clear(self):

        os.system(
            "cls"
            if os.name == "nt"
            else "clear"
        )

    def timestamp(self):

        return datetime.now().strftime(
            "%H:%M:%S"
        )

    def success(self, message, obj):

        print(
            f"{self.colors['lightblack']}"
            f"{self.timestamp()} » "
            f"{self.colors['lightgreen']}SUCC "
            f"{self.colors['lightblack']}• "
            f"{self.colors['white']}{message} : "
            f"{self.colors['lightgreen']}{obj}"
            f"{self.colors['reset']}"
        )

    def error(self, message, obj):

        print(
            f"{self.colors['lightblack']}"
            f"{self.timestamp()} » "
            f"{self.colors['lightred']}ERRR "
            f"{self.colors['lightblack']}• "
            f"{self.colors['white']}{message} : "
            f"{self.colors['lightred']}{obj}"
            f"{self.colors['reset']}"
        )

    def done(self, message, obj):

        print(
            f"{self.colors['lightblack']}"
            f"{self.timestamp()} » "
            f"{self.colors['lightmagenta']}DONE "
            f"{self.colors['lightblack']}• "
            f"{self.colors['white']}{message} : "
            f"{self.colors['lightmagenta']}{obj}"
            f"{self.colors['reset']}"
        )

    def warning(self, message, obj):

        print(
            f"{self.colors['lightblack']}"
            f"{self.timestamp()} » "
            f"{self.colors['lightyellow']}WARN "
            f"{self.colors['lightblack']}• "
            f"{self.colors['white']}{message} : "
            f"{self.colors['lightyellow']}{obj}"
            f"{self.colors['reset']}"
        )

    def info(self, message, obj):

        print(
            f"{self.colors['lightblack']}"
            f"{self.timestamp()} » "
            f"{self.colors['lightblue']}INFO "
            f"{self.colors['lightblack']}• "
            f"{self.colors['white']}{message} : "
            f"{self.colors['lightblue']}{obj}"
            f"{self.colors['reset']}"
        )


log = console()
log.clear()


# ==========================================
# HEADERS
# ==========================================

headers = {

    'accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',

    'accept-language':
    'en-US,en;q=0.5',

    'referer':
    'https://fitgirl-repacks.site/',

    'sec-ch-ua':
    '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',

    'sec-ch-ua-mobile':
    '?0',

    'sec-ch-ua-platform':
    '"Windows"',

    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}


# ==========================================
# REMOVE PROCESSED LINK
# ==========================================

def remove_link(
    processed_link,
    input_file='input.txt'
):

    with open(
        input_file,
        'r',
        encoding='utf-8'
    ) as file:

        links = file.readlines()

    with open(
        input_file,
        'w',
        encoding='utf-8'
    ) as file:

        for link in links:

            if (
                link.strip()
                != processed_link
            ):

                file.write(link)


# ==========================================
# LOAD LINKS
# ==========================================

if not os.path.exists("input.txt"):

    with open(
        "input.txt",
        "w",
        encoding="utf-8"
    ):
        pass

    log.warning(
        "Created input.txt",
        "add links and rerun"
    )

    raise SystemExit(1)


with open(
    'input.txt',
    'r',
    encoding='utf-8'
) as file:

    links = [

        line.strip()

        for line in file

        if line.strip()
    ]


if not links:

    log.warning(
        "input.txt is empty",
        "add links and rerun"
    )

    raise SystemExit(1)


# ==========================================
# OUTPUT FILE
# ==========================================

timestamp = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
)

output_file = (
    f"output_links_{timestamp}.txt"
)

log.info(
    "Output File",
    output_file
)


# ==========================================
# PROCESS LINKS
# ==========================================

total = len(links)

log.info(
    "Total Links",
    total
)

for index, link in enumerate(
    links,
    start=1
):

    try:

        log.info(
            f"[{index}/{total}] Processing",
            f"{link[:60]}..."
        )

        response = requests.get(
            link,
            headers=headers,
            timeout=30
        )

        # ==================================
        # RESPONSE CHECK
        # ==================================

        if response.status_code != 200:

            log.error(
                "Failed To Fetch Page",
                response.status_code
            )

            continue

        # ==================================
        # PARSE HTML
        # ==================================

        soup = BeautifulSoup(
            response.text,
            'html.parser'
        )

        script_tags = soup.find_all(
            'script'
        )

        download_function = None

        for script in script_tags:

            if (
                'function download'
                in script.text
            ):

                download_function = script.text

                break

        # ==================================
        # EXTRACT URL
        # ==================================

        if download_function:

            match = re.search(

                r'window\.open\(["\'](https?://[^\s"\'\)]+)',

                download_function
            )

            if match:

                download_url = match.group(1)

                # ==========================
                # SAVE LINK
                # ==========================

                with open(
                    output_file,
                    "a",
                    encoding="utf-8"
                ) as f:

                    f.write(
                        download_url
                        + "\n"
                    )

                log.success(
                    "Saved Direct Link",
                    f"{download_url[:80]}..."
                )

                # ==========================
                # REMOVE FROM INPUT
                # ==========================

                remove_link(link)

            else:

                log.error(
                    "No Download Url Found",
                    "regex failed"
                )

        else:

            log.error(
                "Download Function Not Found",
                "site changed or protected"
            )

    except Exception as e:

        log.error(
            "Processing Failed",
            str(e)
        )


# ==========================================
# FINISHED
# ==========================================

log.done(
    "All Links Saved To",
    output_file
)