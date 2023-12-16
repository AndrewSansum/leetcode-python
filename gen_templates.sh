#!/bin/bash

echo "Initiialising templates for problem $1"
echo "Creating problem folder"

mkdir "problems/problem$1"

echo "Creating solution file"

touch "problems/problem$1/problem$1.py"

echo "Creating test file"

touch "problems/problem$1/problem${1}_test.py"
cat > problems/problem$1/problem${1}_test.py << EOL
import unittest

from problem$1 import Solution

class Test${1}Solution(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
EOL

echo "Finished"