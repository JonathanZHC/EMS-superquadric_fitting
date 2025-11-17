# 📘 EMS: Probabilistic Superquadric Fitting (Python Implementation)

This document explains **two separate pipelines**:

1. **Pipeline A — Visualizing `.ply` / point cloud files** (Open3D only)
2. **Pipeline B — Running the EMS algorithm to fit superquadrics** (Mayavi + EMS dependencies)

The two pipelines use different conda environments and do **not** depend on each other.

---

# 🔵 Pipeline A — Visualize Point Clouds (Open3D)

This pipeline is only for viewing `.ply` files.

### 1. Create visualization environment

```bash
conda create -n vis python=3.10 -y
conda activate vis
conda install -c conda-forge open3d pyyaml pandas pytz scikit-learn matplotlib scipy h5py tqdm -y
```

### 2. Visualize a PLY file

```bash
python tests/test_visualize_pcd.py examples/<obj.ply>
```

This script loads the `.ply` and visualizes it using **Open3D**.

---

# 🔴 Pipeline B — Fit Superquadric with EMS

This environment is dedicated to running the EMS **probabilistic recovery** algorithm.

### 1. Create EMS environment (strict version constraints)

```bash
conda create -n ems python=3.8 numpy=1.19.2 scipy=1.5.2 numba=0.53.1 -y
conda activate ems
```

Install visualization + PLY loader dependencies:

```bash
conda install -c conda-forge vtk=8.2 mayavi=4.7.1 plyfile -y
```

### 2. Install EMS package

```bash
cd Python
pip install .
```

---

## ▶️ Run EMS to Fit a Superquadric

```bash
python tests/test_script.py examples/<obj.ply> --result --runtime --visualize
```

### Available flags

| Flag          | Effect                                                    |
| ------------- | --------------------------------------------------------- |
| `--result`    | print parameters of recovered superquadric                |
| `--runtime`   | execution time (note: first run triggers JIT compilation) |
| `--visualize` | show point cloud + fitted superquadric via Mayavi         |
