Last login: Sun May 18 11:01:41 on ttys001
Brennan_ORear@MacBook-Air-2 ~ % cd ~/projects/FWE_morphogenesis
head -n 5 data/Inference_Full_Data.csv
Table - Inference_Full Data_data-2
Public ID,Organization,Availability,System Name (click + for details),# of Nodes,Processor,Accelerator,# of Accelerators,Benchmark,Model MLC,Scenario,Units,Valid / Invalid,Division/Power,Operating System,Software,System Type Revised,Version,Division,Division Revised,Has Power,Host Processor Core Count,System Type,Result,Result at System Name
5.0-0023,Fujitsu,available,PRIMERGY CDI (8x H100NVL TensorRT),1,INTEL(R) XEON(R) GOLD 6530,NVIDIA H100-NVL-94GB,8,Inference,gptj-99.9,Server,Tokens/s,,Closed - Power,Ubuntu 24.04,TensorRT 10.8 CUDA 12.8,Datacenter,v5.0,closed,Closed,TRUE,32,datacenter,14846.7,14846.7
5.0-0023,Fujitsu,available,PRIMERGY CDI (8x H100NVL TensorRT),1,INTEL(R) XEON(R) GOLD 6530,NVIDIA H100-NVL-94GB,8,Inference,3d-unet-99.9,Offline,Watts,,Closed - Power,Ubuntu 24.04,TensorRT 10.8 CUDA 12.8,Datacenter,v5.0,closed,Closed,TRUE,32,datacenter,4921.335897436,4921.335897436
5.0-0023,Fujitsu,available,PRIMERGY CDI (8x H100NVL TensorRT),1,INTEL(R) XEON(R) GOLD 6530,NVIDIA H100-NVL-94GB,8,Inference,llama2-70b-interactive-99.9,Server,Queries/s,,Closed - Power,Ubuntu 24.04,TensorRT 10.8 CUDA 12.8,Datacenter,v5.0,closed,Closed,TRUE,32,datacenter,11041.5,11041.5
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
python3 scripts/compute_eta_edge.py
Traceback (most recent call last):
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/indexes/base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Has Power'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/Brennan_ORear/projects/FWE_morphogenesis/scripts/compute_eta_edge.py", line 7, in <module>
    df = df[df['Has Power'] == True]
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Has Power'
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % python3 - <<'PY'
import pandas as pd, textwrap
df = pd.read_csv('data/Inference_Full_Data.csv', nrows=0)   # read only header
print(textwrap.fill(", ".join(df.columns), width=100))
PY
Table - Inference_Full Data_data-2
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % head -n 2 data/Inference_Full_Data.csv
Table - Inference_Full Data_data-2
Public ID,Organization,Availability,System Name (click + for details),# of Nodes,Processor,Accelerator,# of Accelerators,Benchmark,Model MLC,Scenario,Units,Valid / Invalid,Division/Power,Operating System,Software,System Type Revised,Version,Division,Division Revised,Has Power,Host Processor Core Count,System Type,Result,Result at System Name
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % open -a TextEdit scripts/compute_eta_edge.py
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % python3 scripts/compute_eta_edge.py
Traceback (most recent call last):
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/indexes/base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Has Power'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/Brennan_ORear/projects/FWE_morphogenesis/scripts/compute_eta_edge.py", line 12, in <module>
    df = df[df['Has Power'] == True]
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Has Power'
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
python3 scripts/compute_eta_edge.py
Traceback (most recent call last):
  File "/Users/Brennan_ORear/projects/FWE_morphogenesis/scripts/compute_eta_edge.py", line 17, in <module>
    df = df[df['Has Power'].str.upper() == 'TRUE']
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/generic.py", line 6299, in __getattr__
    return object.__getattribute__(self, name)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/accessor.py", line 224, in __get__
    accessor_obj = self._accessor(obj)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/strings/accessor.py", line 191, in __init__
    self._inferred_dtype = self._validate(data)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/core/strings/accessor.py", line 245, in _validate
    raise AttributeError("Can only use .str accessor with string values!")
AttributeError: Can only use .str accessor with string values!
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
python3 scripts/compute_eta_edge.py
✓  wrote data/edge_eta_single_scale.csv
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % head data/edge_eta_single_scale.csv
System Name (click + for details),Scenario,Model MLC,eta
PRIMERGY CDI (8x H100NVL TensorRT),Server,gptj-99.9,36412.98265624107
PRIMERGY CDI (8x H100NVL TensorRT),Server,llama2-70b-interactive-99.9,27364.583399361836
PRIMERGY CDI (8x H100NVL TensorRT),Offline,rgat,289330.4810555147
PRIMERGY CDI (8x H100NVL TensorRT),Offline,retinanet,28146.362906955386
PRIMERGY CDI (8x H100NVL TensorRT),Offline,3d-unet-99,111.31279250526386
PRIMERGY CDI (8x H100NVL TensorRT),Server,llama2-70b-99,41454.65104363338
PRIMERGY CDI (8x H100NVL TensorRT),Offline,llama2-70b-interactive-99.9,39387.026977657675
PRIMERGY CDI (8x H100NVL TensorRT),Offline,3d-unet-99.9,111.31279250526386
PRIMERGY CDI (8x H100NVL TensorRT),Server,retinanet,25928.70479914054
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % python3 - <<'PY'
import pandas as pd
df = pd.read_csv('data/edge_eta_single_scale.csv')
print(df['eta'].describe())
PY

count        19.000000
mean      51615.170874
std       61943.617100
min         111.312793
25%       27755.473153
50%       36499.070660
75%       43165.246612
max      289330.481056
Name: eta, dtype: float64
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % 
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % # data separation
mkdir -p data/raw   data/processed

# code & docs
mkdir -p scripts notebooks docs
zsh: command not found: #
[1] 30679
zsh: command not found: #
[1]  + exit 127   # code
zsh: command not found: docs
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % # raw MLPerf CSV
mv data/Inference_Full_Data.csv       data/raw/inference_v5_full.csv

# processed η table
mv data/edge_eta_single_scale.csv     data/processed/

# GPU efficiency & spectrum (already properly named)
mv data/gpu_efficiency.csv            data/processed/
mv data/gpu_eta_spectrum.png          data/processed/

# chemostat helper script you drafted earlier (if present)
# mv scripts/extract_chemostat.py      scripts/

# ensure the latest compute script is in scripts/
mv scripts/compute_eta_edge.py         scripts/
zsh: command not found: #
zsh: command not found: #
[1] 30691
zsh: command not found: #
zsh: number expected
[1]  + exit 127   # GPU efficiency
mv: rename data/gpu_efficiency.csv to data/processed/gpu_efficiency.csv: No such file or directory
mv: rename data/gpu_eta_spectrum.png to data/processed/gpu_eta_spectrum.png: No such file or directory
zsh: unknown file attribute: i
zsh: command not found: #
zsh: command not found: #
mv: scripts/compute_eta_edge.py and scripts/compute_eta_edge.py are identical
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % # ----------------------------
; make the canonical folders
# ----------------------------
mkdir -p data/raw
mkdir -p data/processed
mkdir -p scripts
mkdir -p notebooks
mkdir -p docs
zsh: command not found: #
make: *** No rule to make target `the'.  Stop.
zsh: command not found: #
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % mkdir -p data/raw
mkdir -p data/processed
mkdir -p scripts
mkdir -p notebooks
mkdir -p docs
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % mv -i data/Inference_Full_Data.csv  data/raw/inference_v5_full.csv

mv: data/Inference_Full_Data.csv: No such file or directory
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % mv -i data/edge_eta_single_scale.csv  data/processed/
mv: data/edge_eta_single_scale.csv: No such file or directory
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
ls -R1 data | sed 's/^/   /'
   efficiency_by_octave.csv
   energy_by_octave.csv
   entropy_by_octave.csv
   eta_spectrum.png
   imaging_processed
   imaging_raw
   Inference_Full_Data.csv.numbers
   o2_curves.csv
   o2_raw.csv
   processed
   raw
   
   data/imaging_processed:
   octave_frames
   
   data/imaging_processed/octave_frames:
   frame_16min.tif
   frame_1min.tif
   frame_2min.tif
   frame_302min.tif
   frame_32min.tif
   frame_4min.tif
   frame_64min.tif
   frame_8min.tif
   
   data/imaging_raw:
   zebra_gastrulation.tif
   zebrafish_confocal_gastrulation.lsm
   zebrafish_confocal_gastrulation.tif
   
   data/processed:
   edge_eta_single_scale.csv
   
   data/raw:
   inference_v5_full.csv
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % mkdir -p data/raw
mkdir -p data/processed
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % mv data/Inference_Full_Data.csv  data/raw/inference_v5_full.csv
mv: data/Inference_Full_Data.csv: No such file or directory
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % mv data/edge_eta_single_scale.csv  data/processed/
mv: data/edge_eta_single_scale.csv: No such file or directory
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
mv -i data/efficiency_by_octave.csv  data/processed/
mv -i data/energy_by_octave.csv      data/processed/
mv -i data/entropy_by_octave.csv     data/processed/
mv -i data/eta_spectrum.png          data/processed/
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % open -a TextEdit scripts/compute_eta_edge.py
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % python3 scripts/compute_eta_edge.py
Traceback (most recent call last):
  File "/Users/Brennan_ORear/projects/FWE_morphogenesis/scripts/compute_eta_edge.py", line 9, in <module>
    df = pd.read_csv('data/Inference_Full_Data.csv', skiprows=1)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/io/parsers/readers.py", line 1026, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/io/parsers/readers.py", line 620, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/io/parsers/readers.py", line 1620, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/io/parsers/readers.py", line 1880, in _make_engine
    self.handles = get_handle(
  File "/Users/Brennan_ORear/Library/Python/3.9/lib/python/site-packages/pandas/io/common.py", line 873, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'data/Inference_Full_Data.csv'
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % open -a TextEdit scripts/compute_eta_edge.py
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects/FWE_morphogenesis
python3 scripts/compute_eta_edge.py
✓  wrote data/processed/edge_eta_single_scale.csv
Brennan_ORear@MacBook-Air-2 FWE_morphogenesis % cd ~/projects
mv FWE_morphogenesis FWE_examples
cd FWE_examples
Brennan_ORear@MacBook-Air-2 FWE_examples % git init
echo '__pycache__/' > .gitignore
echo '*.pyc'        >> .gitignore
echo '*~'           >> .gitignore

git add data scripts notebooks docs .gitignore
git commit -m "Initial commit of FWE_examples project"

# create empty repo on GitHub named FWE_examples, copy the HTTPS URL
git remote add origin https://github.com/<User>/FWE_examples.git
git branch -M main
git push -u origin main
Initialized empty Git repository in /Users/Brennan_ORear/projects/FWE_examples/.git/
[main (root-commit) 8204615] Initial commit of FWE_examples project
 Committer: Brennan O'Rear <Brennan_ORear@MacBook-Air-2.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 32 files changed, 783 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 data/.DS_Store
 create mode 100644 data/Inference_Full_Data.csv.numbers
 create mode 100644 data/imaging_processed/octave_frames/frame_16min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_1min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_2min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_302min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_32min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_4min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_64min.tif
 create mode 100644 data/imaging_processed/octave_frames/frame_8min.tif
 create mode 100644 data/imaging_raw/zebra_gastrulation.tif
 create mode 100644 data/imaging_raw/zebrafish_confocal_gastrulation.lsm
 create mode 100644 data/imaging_raw/zebrafish_confocal_gastrulation.tif
 create mode 100644 data/o2_curves.csv
 create mode 100644 data/o2_raw.csv
 create mode 100644 data/processed/edge_eta_single_scale.csv
 create mode 100644 data/processed/efficiency_by_octave.csv
 create mode 100644 data/processed/energy_by_octave.csv
 create mode 100644 data/processed/entropy_by_octave.csv
 create mode 100644 data/processed/eta_spectrum.png
 create mode 100644 data/raw/inference_v5_full.csv
 create mode 100755 scripts/02_entropy_windows.py
 create mode 100755 scripts/03_align_energy.py
 create mode 100755 scripts/04_compute_eta.py
 create mode 100644 scripts/compute_eta_edge.py
 create mode 100755 scripts/compute_eta_gpu.py
 create mode 100755 scripts/convert_ocr_to_joules.py
 create mode 100755 scripts/extract_octaves.py
 create mode 100755 scripts/inspect_lsm.py
 create mode 100755 scripts/lsm_to_tif.py
 create mode 100755 scripts/quickprobe_gpu.py
zsh: command not found: #
zsh: no such file or directory: User
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
Brennan_ORear@MacBook-Air-2 FWE_examples % cd ~/projects/FWE_examples 
git remote add origin https://github.com/brennanlives/FWE_examples.git
git branch -M main
git push -u origin main
Username for 'https://github.com': brennanlives
Password for 'https://brennanlives@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/brennanlives/FWE_examples.git/'
Brennan_ORear@MacBook-Air-2 FWE_examples %  % cd ~/projects/FWE_examples
git remote add origin https://github.com/brennanlives/FWE_examples.git
git branch -M main
git push -u origin main

fg: no current job
error: remote origin already exists.
Username for 'https://github.com': brennanlives
Password for 'https://brennanlives@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/brennanlives/FWE_examples.git/'
Brennan_ORear@MacBook-Air-2 FWE_examples % git config --global credential.helper osxkeychain
Brennan_ORear@MacBook-Air-2 FWE_examples % cd ~/projects/FWE_examples 
git push -u origin main
Username for 'https://github.com': brennanlives
Password for 'https://brennanlives@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/brennanlives/FWE_examples.git/'
Brennan_ORear@MacBook-Air-2 FWE_examples % cd ~/projects/FWE_examples 
git push -u origin main
Username for 'https://github.com': brennanlives
Password for 'https://brennanlives@github.com': 
remote: Repository not found.
fatal: repository 'https://github.com/brennanlives/FWE_examples.git/' not found
Brennan_ORear@MacBook-Air-2 FWE_examples % cd ~/projects/FWE_examples 
# try the push again—paste the token when asked for the password
git push -u origin main
zsh: command not found: #
Username for 'https://github.com': brennanlives
Password for 'https://brennanlives@github.com': 
Enumerating objects: 40, done.
Counting objects: 100% (40/40), done.
Delta compression using up to 8 threads
Compressing objects: 100% (35/35), done.
Writing objects: 100% (40/40), 36.57 MiB | 5.21 MiB/s, done.
Total 40 (delta 7), reused 2 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (7/7), done.
remote: error: Trace: 627813d18ed8b5377fb6d2d1836730ed7fc8019fe81ba281c8fee6a37b14603e
remote: error: See https://gh.io/lfs for more information.
remote: error: File data/imaging_raw/zebrafish_confocal_gastrulation.tif is 1662.05 MB; this exceeds GitHub's file size limit of 100.00 M
remote: error: File data/imaging_raw/zebrafish_confocal_gastrulation.lsm is 1984.10 MB; this exceeds GitHub's file size limit of 100.00 M
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/brennanlives/FWE_examples.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/brennanlives/FWE_examples.git'
Brennan_ORear@MacBook-Air-2 FWE_examples % echo 'data/imaging_raw/' >> .gitignore
Brennan_ORear@MacBook-Air-2 FWE_examples % git rm --cached data/imaging_raw/zebrafish_confocal_gastrulation.tif
git rm --cached data/imaging_raw/zebrafish_confocal_gastrulation.lsm
git commit -m "Stop tracking raw imaging files; keep only locally"
rm 'data/imaging_raw/zebrafish_confocal_gastrulation.tif'
rm 'data/imaging_raw/zebrafish_confocal_gastrulation.lsm'
[main 02eb4f4] Stop tracking raw imaging files; keep only locally
 Committer: Brennan O'Rear <Brennan_ORear@MacBook-Air-2.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 data/imaging_raw/zebrafish_confocal_gastrulation.lsm
 delete mode 100644 data/imaging_raw/zebrafish_confocal_gastrulation.tif
Brennan_ORear@MacBook-Air-2 FWE_examples % # install filter-repo if you do not have it
brew install git-filter-repo        # macOS Homebrew

# remove the two paths from all commits
git filter-repo --path data/imaging_raw/zebrafish_confocal_gastrulation.tif \
                --path data/imaging_raw/zebrafish_confocal_gastrulation.lsm --invert-paths
zsh: command not found: #
zsh: command not found: brew
zsh: command not found: #
git: 'filter-repo' is not a git command. See 'git --help'.
Brennan_ORear@MacBook-Air-2 FWE_examples % git push origin main --force
Enumerating objects: 44, done.
Counting objects: 100% (44/44), done.
Delta compression using up to 8 threads
Compressing objects: 100% (39/39), done.
Writing objects: 100% (44/44), 36.57 MiB | 5.31 MiB/s, done.
Total 44 (delta 9), reused 2 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (9/9), done.
remote: error: Trace: 57a25d02272a3063682c85b18fb150af13828a1984b0b65d28d219cff4f0db21
remote: error: See https://gh.io/lfs for more information.
remote: error: File data/imaging_raw/zebrafish_confocal_gastrulation.lsm is 1984.10 MB; this exceeds GitHub's file size limit of 100.00 M
remote: error: File data/imaging_raw/zebrafish_confocal_gastrulation.tif is 1662.05 MB; this exceeds GitHub's file size limit of 100.00 M
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
To https://github.com/brennanlives/FWE_examples.git
 ! [remote rejected] main -> main (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/brennanlives/FWE_examples.git'
Brennan_ORear@MacBook-Air-2 FWE_examples % #!/usr/bin/env bash
set -e

echo "Downloading zebrafish 4-D microscopy stack (~1.9 GB)…"
curl -L -o data/imaging_raw/zebrafish_confocal_gastrulation.lsm \
     "https://zenodo.org/record/1211599/files/cxcr4aMO2_290112.lsm?download=1"

echo "Converting to TIFF (optional)…"
python scripts/lsm_to_tif.py      # you already have this script
zsh: event not found: /usr/bin/env
Brennan_ORear@MacBook-Air-2 FWE_examples % chmod +x scripts/get_large_data.sh
chmod: scripts/get_large_data.sh: No such file or directory
Brennan_ORear@MacBook-Air-2 FWE_examples % chmod +x scripts/get_large_data.sh
chmod: scripts/get_large_data.sh: No such file or directory
Brennan_ORear@MacBook-Air-2 FWE_examples % cd ~/projects/FWE_examples          # make sure you’re at the repo root
mkdir -p scripts                    # in case it doesn’t exist
nano scripts/get_large_data.sh      # or use: open -a TextEdit scripts/get_large_data.sh
cd: too many arguments

  UW PICO 5.09       File: scripts/get_large_data.sh       Modified  

#!/usr/bin/env bash
set -euo pipefail

mkdir -p data/imaging_raw

echo "⬇️️ ️️  Downloading zebrafish 4-D microscopy stack (~1.9 GB)…"
curl -L -o data/imaging_raw/zebrafish_confocal_gastrulation.lsm \
  "https://zenodo.org/record/1211599/files/cxcr4aMO2_290112.lsm?down$

echo "🗜   (Optional) Converting .lsm →  .tif …" 
python3 scripts/lsm_to_tif.py      # requires tifffile; you already $
                        
                               







^G Get Help^O WriteOut^R Read Fil^Y Prev Pg ^K Cut Text^C Cur Pos 
^X Exit    ^J Justify ^W Where is^V Next Pg ^U UnCut Te^T To Spell
