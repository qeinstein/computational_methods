# Computational Methods Course Repository

Comprehensive resource for CSC205 - Computational Methods at the University of Lagos

## Overview
This repository contains explanations, implementations, and examples for all major topics in computational methods. Each topic is organized with both theoretical explanations (markdown files) and practical implementations (Python files).

---

## Folder Structure

```
computational_methods/
│
├── 01_Introduction_to_Programming/
│   ├── README.md
│   ├── 01_python_basics.md
│   ├── 01_python_basics.py
│   ├── 02_oop.md
│   ├── 02_oop.py
│   ├── 03_visualization.md
│   └── 03_visualization.py
│
├── 02_Computing_Fundamentals_and_Error_Analysis/
│   ├── README.md
│   ├── 01_number_representation.md
│   ├── 01_number_representation.py
│   ├── 02_error_types.md
│   ├── 02_error_types.py
│   ├── 03_debugging_practices.md
│   └── 03_debugging_practices.py
│
├── 03_Root_Finding/
│   ├── README.md
│   ├── 01_bisection_method.md
│   ├── 01_bisection_method.py
│   ├── 02_newton_raphson.md
│   ├── 02_newton_raphson.py
│   ├── 03_secant_method.md
│   └── 03_secant_method.py
│
├── 04_Numerical_Differentiation/
│   ├── README.md
│   ├── 01_forward_difference.md
│   ├── 01_forward_difference.py
│   ├── 02_backward_difference.md
│   ├── 02_backward_difference.py
│   ├── 03_center_difference.md
│   └── 03_center_difference.py
│
├── 05_Numerical_Integration/
│   ├── README.md
│   ├── 01_trapezoidal_rule.md
│   ├── 01_trapezoidal_rule.py
│   ├── 02_simpsons_rule.md
│   └── 02_simpsons_rule.py
│
├── 06_Differential_Equations/
│   ├── README.md
│   ├── 01_euler_method.md
│   ├── 01_euler_method.py
│   ├── 02_heun_improved_euler.md
│   ├── 02_heun_improved_euler.py
│   ├── 03_runge_kutta.md
│   └── 03_runge_kutta.py
│
├── 07_Interpolation/
│   ├── README.md
│   ├── 01_linear_spline.md
│   ├── 01_linear_spline.py
│   ├── 02_quadratic_spline.md
│   ├── 02_quadratic_spline.py
│   ├── 03_cubic_spline.md
│   └── 03_cubic_spline.py
│
├── 08_Fourier_Transforms/
│   ├── README.md
│   ├── 01_discrete_fourier_transform.md
│   ├── 01_discrete_fourier_transform.py
│   ├── 02_fast_fourier_transform.md
│   └── 02_fast_fourier_transform.py
│
├── 09_Linear_Algebra/
│   ├── README.md
│   ├── 01_lu_decomposition.md
│   ├── 01_lu_decomposition.py
│   ├── 02_gaussian_elimination.md
│   ├── 02_gaussian_elimination.py
│   ├── 03_jacobi_method.md
│   └── 03_jacobi_method.py
│
└── README.md (this file)
```

---

## How to Use This Repository

1. **For Learning**: Start with the markdown files (`.md`) in each folder for theory, then review the Python files (`.py`) for implementation
2. **For Reference**: Each `.py` file contains documented functions with examples
3. **Progressive Learning**: Topics are ordered from fundamentals to advanced concepts

---

## Advice for Sharing

### 1. **Folder Organization Strategy**
   - Number each folder (01_, 02_, etc.) so they appear in logical order in file explorers
   - Use clear, descriptive folder names separated by underscores
   - Keep each topic self-contained in its own directory

### 2. **File Naming Convention**
   - Pair each explanation file with its implementation: `01_topic.md` with `01_topic.py`
   - Use lowercase with underscores for file names
   - This makes it easy to find corresponding files

### 3. **Content Structure for Each Folder**
   - **README.md**: Overview of the topic with key concepts (quick summary)
   - **XX_concept.md**: Theory, formulas, step-by-step explanation
   - **XX_concept.py**: Implementations with:
     - Clear function names
     - Docstrings explaining parameters and returns
     - Example usage/test cases at the bottom
     - Comments for complex logic

### 4. **Python File Best Practices**
   ```python
   def function_name(param1, param2):
       """
       Brief description
       
       Parameters:
       -----------
       param1 : type
           Description
       
       Returns:
       --------
       result : type
           Description
       
       Example:
       --------
       >>> result = function_name(1, 2)
       """
       pass
   
   # Example usage
   if __name__ == "__main__":
       # Your test cases here
       pass
   ```

### 5. **Distribution Tips**
   - Use GitHub or GitLab (free, version control, easy to share)
   - Alternatively: ZIP file with clear structure
   - Add a `.gitignore` file to exclude `__pycache__/` and `.pyc` files
   - Include `requirements.txt` if using external libraries (numpy, matplotlib, scipy)

### 6. **Documentation Standards**
   - Keep markdown files concise but complete
   - Use headers, bullet points, and code blocks for clarity
   - Include 2-3 worked examples per topic
   - Link between related topics (e.g., "see 03_Root_Finding for context")

### 7. **Version Control (if using Git)**
   Create a `.gitignore` file:
   ```
   __pycache__/
   *.pyc
   *.pyo
   .DS_Store
   .vscode/
   .idea/
   *.egg-info/
   ```

### 8. **Optional Enhancements**
   - Add a `requirements.txt` for dependencies
   - Include a main `CONTRIBUTING.md` if coursemates will add content
   - Add test files (`test_XX_concept.py`) for verification
   - Create a `notebooks/` folder for Jupyter notebooks if preferred

---

## Recommended Learning Path

1. Start with **01 - Introduction to Programming** (refresh Python skills)
2. Move to **02 - Computing Fundamentals** (understand errors and debugging)
3. Progress through **03-05** (core numerical methods)
4. Study **06-09** (advanced topics)

---

## Contributors

- Created for CSC205 Computational Methods Course

---

**Last Updated**: February 2026