import numpy as np

# Embedding of Person A.
embedding_1 = np.array(
    [1, 2, 3]
)

# Similar embedding.
embedding_2 = np.array(
    [1, 2, 4]
)

# Different embedding.
embedding_3 = np.array(
    [10, 20, 30]
)

# Calculate distance.
distance_1 = np.linalg.norm(
    embedding_1 - embedding_2
)

distance_2 = np.linalg.norm(
    embedding_1 - embedding_3
)

print(
    f"Distance 1 : {distance_1}"
)

print(
    f"Distance 2 : {distance_2}"
)