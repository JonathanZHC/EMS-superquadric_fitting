## Guidelines for Python Implementation

This is the guideline and structual explanation of the Python implementation of the EMS algorithm.

### Dependency

The code is tested under Python 3.8.8, but should have little compatibility concerns.
The following packages are required to run the EMS algorithm:

1. numpy 1.19.2
2. scipy 1.5.2
3. numba 0.53.1 -- for acceleration based on JIT (Just-In-Time compiler)


For demo, the following packages are needed:

1. plyfile -- for loading `.ply` point cloud files
2. mayavi -- for visualization of meshes and point clouds

### Installation

We recommend to install the EMS package with conda.

1. Create a conda env called 'ems':

```bash
conda create -n ems python=3.8
conda activate ems
```

2. Add relevant dependency:

```bash
conda install numpy=1.19.2 scipy=1.5.2
conda install numba=0.53.1

conda install -c conda-forge vtk=8.2
conda install -c conda-forge mayavi=4.7.1
```

3. Change directory to `/Python` folder:

```
cd /Python
```

4. Install the whole package:

```
pip install .
```
    

### Run Demo

The demo script is `/Python/tests/test_script.py`. The demo reads a `.ply` point cloud and returns the parameters of the recovered superquadric, runtime, and visualization as required.

For example, in terminal type in

```
python tests/test_script.py examples/<obj.ply> --result --runtime --visualize
```

Note the first run of the code takes longer, since the JIT will translate the Python and NumPy code into fast machine code (and will be cached for futher calls).
