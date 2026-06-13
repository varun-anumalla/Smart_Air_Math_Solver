import mediapipe as mp

print(mp.__file__)

try:
    from mediapipe.python import solutions
    print("SUCCESS")
except Exception as e:
    print("ERROR:", e)