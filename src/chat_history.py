import json
import os


# ============================================================
# CHAT HISTORY DIRECTORY
# ============================================================

CHAT_DIR = "data/chat"

CHAT_FILE = os.path.join(
    CHAT_DIR,
    "conversation.json"
)


# ============================================================
# CREATE DIRECTORY
# ============================================================

def create_chat_directory():

    os.makedirs(
        CHAT_DIR,
        exist_ok=True
    )


# ============================================================
# LOAD HISTORY
# ============================================================

def load_chat_history():

    create_chat_directory()

    if not os.path.exists(CHAT_FILE):

        return []


    try:

        with open(
            CHAT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except (
        json.JSONDecodeError,
        OSError
    ):

        return []


# ============================================================
# SAVE HISTORY
# ============================================================

def save_chat_history(history):

    create_chat_directory()

    with open(
        CHAT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# ADD MESSAGE
# ============================================================

def add_message(
    role,
    message
):

    history = load_chat_history()

    history.append({

        "role": role,

        "message": message

    })

    save_chat_history(
        history
    )


# ============================================================
# GET HISTORY
# ============================================================

def get_history():

    return load_chat_history()


# ============================================================
# CLEAR HISTORY
# ============================================================

def clear_history():

    if os.path.exists(CHAT_FILE):

        os.remove(
            CHAT_FILE
        )


# ============================================================
# FORMAT HISTORY FOR GEMINI
# ============================================================

def format_history():

    history = load_chat_history()

    if not history:

        return "No previous conversation."


    formatted = []

    for item in history:

        role = item.get(
            "role",
            "unknown"
        )

        message = item.get(
            "message",
            ""
        )

        formatted.append(
            f"{role.upper()}: {message}"
        )


    return "\n".join(
        formatted
    )