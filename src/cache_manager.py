import os
import json
import hashlib


# ============================================================
# CACHE DIRECTORY
# ============================================================

CACHE_DIR = "data/cache"

CACHE_FILE = os.path.join(
    CACHE_DIR,
    "response_cache.json"
)


# ============================================================
# CREATE CACHE DIRECTORY
# ============================================================

def create_cache_directory():

    os.makedirs(
        CACHE_DIR,
        exist_ok=True
    )


# ============================================================
# CREATE CACHE KEY
# ============================================================

def create_cache_key(question, context):

    """
    Create a unique key for the question + context.
    """

    text = question + "\n" + context

    key = hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()

    return key


# ============================================================
# LOAD CACHE
# ============================================================

def load_cache():

    create_cache_directory()

    if not os.path.exists(CACHE_FILE):

        return {}


    try:

        with open(
            CACHE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    except (
        json.JSONDecodeError,
        OSError
    ):

        return {}


# ============================================================
# SAVE CACHE
# ============================================================

def save_cache(cache):

    create_cache_directory()

    with open(
        CACHE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            cache,
            file,
            indent=4,
            ensure_ascii=False
        )


# ============================================================
# GET CACHED ANSWER
# ============================================================

def get_cached_answer(
    question,
    context
):

    cache = load_cache()

    key = create_cache_key(
        question,
        context
    )

    return cache.get(key)


# ============================================================
# STORE ANSWER
# ============================================================

def store_cached_answer(
    question,
    context,
    answer
):

    cache = load_cache()

    key = create_cache_key(
        question,
        context
    )

    cache[key] = {
        "question": question,
        "answer": answer
    }

    save_cache(cache)


# ============================================================
# CACHE STATISTICS
# ============================================================

def get_cache_statistics():

    cache = load_cache()

    return {
        "total_cached_answers": len(cache)
    }


# ============================================================
# CLEAR CACHE
# ============================================================

def clear_cache():

    if os.path.exists(CACHE_FILE):

        os.remove(
            CACHE_FILE
        )