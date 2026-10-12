
import json
import sys

MINIMUM_ACCURACY = 0.99

with open("metrics.json") as f:
    metrics = json.load(f)

accuracy = metrics["accuracy"]

print("Model accuracy:", round(accuracy, 4))
print("Required accuracy:", MINIMUM_ACCURACY)

if accuracy < MINIMUM_ACCURACY:
    print("QUALITY GATE FAILED")
    sys.exit(1)

print("QUALITY GATE PASSED")
sys.exit(0)
