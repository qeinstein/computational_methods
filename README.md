# CSC205 Course Repository

Resource for CSC205(uniLAG)

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

## Usage

1. **For Learning**: Start with the markdown files (`.md`) in each folder for theory, then review the Python files (`.py`) for implementation
2. **For Reference**: Each `.py` file contains documented functions with examples

### Setting up a virtual environment (Linux)

Follow these commands to create and activate a Python virtual environment and install dependencies:

```bash
python3 -m venv venv | python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

When finished, deactivate the environment with:

```bash
deactivate
```

---

## Recommendation

1. Start with **01 - Introduction to Programming** (refresh Python skills)
2. Move to **02 - Computing Fundamentals** (understand errors and debugging)
3. Progress through **03-05** (core numerical methods)
4. Study **06-09** (advanced topics)

---

## Contributors

- Fluxx
- Created for CSC205 Computational Methods Course

---

**Last Updated**: February 2026