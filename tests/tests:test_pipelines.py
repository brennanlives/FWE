import subprocess, pathlib, pandas as pd

def test_wetland_runs(tmp_path):
    out = tmp_path / "eta_wetland.csv"
    subprocess.check_call(["python3", "src/compute_eta_wetland.py"])
    assert pathlib.Path("results/eta_wetland.csv").is_file()

def test_microbe_runs(tmp_path):
    out = tmp_path / "eta_microbe.csv"
    subprocess.check_call(["python3", "src/compute_eta_microbe.py"])
    df = pd.read_csv("results/eta_microbe.csv")
    assert df["eta"].notna().all() and df["eta"].lt(1e6).all()