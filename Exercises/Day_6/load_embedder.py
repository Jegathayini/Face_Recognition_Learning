import mediapipe as mp

# Load embedder model.
embedder = mp.tasks.vision.ImageEmbedder.create_from_model_path(
    "Models/mobilenet_v3_small.tflite"
)

print(
    "Embedder Loaded Successfully ✅"
)
