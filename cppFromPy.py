import subprocess

# Write C++ code to a file
cpp_code = """
#include <iostream>
int main() {
    int x = 6;
    std::cout << x << std::endl;
    return 0;
}
"""
with open('example.cpp', 'w') as f:
    f.write(cpp_code)

# Compile the C++ code
subprocess.run(['g++', 'example.cpp', '-o', 'example'])

# Run the compiled program
subprocess.run(['./example'])
