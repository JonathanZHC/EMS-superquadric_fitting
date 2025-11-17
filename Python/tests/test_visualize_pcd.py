#!/usr/bin/env python3
import open3d as o3d
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize_ply_open3d.py file.ply")
        sys.exit(1)

    path = sys.argv[1]
    print(f"Loading: {path}")

    pcd = o3d.io.read_point_cloud(path)
    if len(pcd.points) == 0:
        print("Error: no points found. Is this a valid PLY file?")
        sys.exit(1)

    print(f"Loaded {len(pcd.points)} points.")

    o3d.visualization.draw_geometries([pcd])

if __name__ == "__main__":
    main()
