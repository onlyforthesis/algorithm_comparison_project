import sys
import os
print("Python version:", sys.version)
print("Current directory:", os.getcwd())
print("Python path:", sys.path[:3])

try:
    import matplotlib
    print("✅ matplotlib available:", matplotlib.__version__)
except ImportError as e:
    print("❌ matplotlib error:", e)

try:
    import numpy
    print("✅ numpy available:", numpy.__version__)
except ImportError as e:
    print("❌ numpy error:", e)

try:
    import pandas
    print("✅ pandas available:", pandas.__version__)
except ImportError as e:
    print("❌ pandas error:", e)

print("Test completed successfully!")
