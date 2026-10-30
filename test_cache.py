from src.llm import generate_answer

from src.cache_manager import (
    get_cache_statistics
)


question = (
    "What are the main technologies "
    "used in these research papers?"
)


context = """
Paper 1 uses machine learning,
Python and TensorFlow.

Paper 2 uses deep learning,
CNN and PyTorch.

Paper 3 uses natural language processing
and transformer models.
"""


print("\n")
print("=" * 60)
print("RESEARCHMIND AI - CACHE TEST")
print("=" * 60)


# ============================================================
# FIRST REQUEST
# ============================================================

print("\nFIRST REQUEST")

answer1 = generate_answer(
    question,
    context
)

print("\nANSWER:")
print(answer1)


# ============================================================
# SECOND REQUEST
# ============================================================

print("\n")
print("=" * 60)

print("\nSECOND REQUEST")

answer2 = generate_answer(
    question,
    context
)

print("\nANSWER:")
print(answer2)


# ============================================================
# CACHE STATISTICS
# ============================================================

stats = get_cache_statistics()


print("\n")
print("=" * 60)
print("CACHE STATISTICS")
print("=" * 60)

print(
    f"\nCached answers: "
    f"{stats['total_cached_answers']}"
)