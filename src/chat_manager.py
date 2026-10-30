import os
import json
import uuid


# ============================================================
# CHAT STORAGE LOCATION
# ============================================================

CHAT_FOLDER = os.path.join(
    "data",
    "chats"
)

CHAT_FILE = os.path.join(
    CHAT_FOLDER,
    "chats.json"
)


# ============================================================
# MAKE SURE CHAT FOLDER EXISTS
# ============================================================

def ensure_chat_storage():

    os.makedirs(
        CHAT_FOLDER,
        exist_ok=True
    )


# ============================================================
# LOAD CHATS FROM JSON
# ============================================================

def load_chats():

    ensure_chat_storage()

    if not os.path.exists(CHAT_FILE):

        return []

    try:

        with open(
            CHAT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            chats = json.load(file)

        if isinstance(chats, list):

            return chats

        return []

    except (
        json.JSONDecodeError,
        OSError
    ):

        return []


# ============================================================
# SAVE CHATS TO JSON
# ============================================================

def save_chats(chats):

    ensure_chat_storage()

    temporary_file = (
        CHAT_FILE + ".tmp"
    )

    with open(
        temporary_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chats,
            file,
            indent=4,
            ensure_ascii=False
        )

    os.replace(
        temporary_file,
        CHAT_FILE
    )


# ============================================================
# CREATE NEW CHAT
# ============================================================

def create_chat(
    title="New Research Chat"
):

    chat_id = str(
        uuid.uuid4()
    )

    return {
        "id": chat_id,
        "title": title,
        "messages": []
    }


# ============================================================
# ADD MESSAGE
# ============================================================

def add_message(
    chat,
    role,
    content
):

    chat["messages"].append(
        {
            "role": role,
            "content": content
        }
    )


# ============================================================
# DELETE CHAT
# ============================================================

def delete_chat(
    chats,
    chat_id
):

    return [
        chat
        for chat in chats
        if chat.get("id") != chat_id
    ]


# ============================================================
# FIND CHAT
# ============================================================

def get_chat(
    chats,
    chat_id
):

    for chat in chats:

        if chat.get("id") == chat_id:

            return chat

    return None


# ============================================================
# GENERATE CHAT TITLE
# ============================================================

def generate_chat_title(
    question
):

    question = question.strip()

    if not question:

        return "New Research Chat"

    words = question.split()

    title = " ".join(
        words[:6]
    )

    if len(words) > 6:

        title += "..."

    return title


# ============================================================
# UPDATE CHAT TITLE
# ============================================================

def update_chat_title(
    chat,
    question
):

    chat["title"] = generate_chat_title(
        question
    )


# ============================================================
# ADD CHAT
# ============================================================

def add_chat(
    chats,
    chat
):

    chats.append(
        chat
    )

    save_chats(
        chats
    )

    return chats


# ============================================================
# SAVE AFTER MESSAGE
# ============================================================

def save_chat_message(
    chats,
    chat
):

    for index, existing_chat in enumerate(
        chats
    ):

        if existing_chat.get("id") == chat.get("id"):

            chats[index] = chat

            break

    save_chats(
        chats
    )

    return chats


# ============================================================
# REMOVE CHAT AND SAVE
# ============================================================

def remove_chat(
    chats,
    chat_id
):

    updated_chats = delete_chat(
        chats,
        chat_id
    )

    save_chats(
        updated_chats
    )

    return updated_chats