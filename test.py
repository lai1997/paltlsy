import os
import shutil
import zipfile
import os
import subprocess

# subprocess.run(['rm', '-r', 'content'])
# subprocess.run(['git', 'clone', 'https://github.com/t7uIqs22H10c/paltlsy'])
# subprocess.run(['mkdir', '-p', 'content'])
# subprocess.run(['mv', 'paltlsy/', 'content/paltlsy'])
#
# with zipfile.ZipFile('./content/paltlsy/cav-2024-submission-5511.zip', 'r') as zip_ref:
#     zip_ref.extractall('./content/paltlsy/')
#
# contents = os.listdir("./content/paltlsy/cav-2024-submission-5511")
# for item in contents:
#     source_path = os.path.join("./content/paltlsy/cav-2024-submission-5511", item)
#     destination_path = os.path.join("./content/paltlsy/", item)
#     shutil.move(source_path, destination_path)
#
# print("Compiling...")
# subprocess.run(['nvcc', '--extended-lambda', '-I', './content/paltlsy/code/modified_libraries', './content/paltlsy/code/ltli6463.cu', '-o','ltli64630'])

gpu_info = "nvidia-smi"
if subprocess.run(gpu_info, capture_output=True, text=True).stdout.find('failed') >= 0:
  print('Not connected to a GPU')
  print("At 'Runtime > Change runtime type', please choose `GPU` for `Hardware accelerator`")
else:
    # subprocess.run(['./ltli64630', './content/paltlsy/benchmarks/existing_work/RQ1_benchmarks/flie_benchmarks/TracesFiles/abscence/Ab0.trace',
    #                 '1', '1', '1', '1', '1', '1', '1', '1', '500', '1', '2'])
    # subprocess.run(['./ltli64630', './cav-2024-submission-5511/datalog/0.trace',
    #                 '1', '1', '1', '1', '1', '1', '1', '1', '500', '1', '2'])
    subprocess.run(['./ltli64630', './cav-2024-submission-5511/datalog/3.trace',
                    '1', '1', '1', '1', '1000', '1000', '1000', '1000', '1000', '1', '2'])

# (~(a ^ b))^(a | b)
#
# t(X,Y) :- (b | c), (~(b ^ c)).

# t(X,Y) :- borc(X,Z), nbc_(Z,Y).
# borc(X,Y) :- b(X,Y).
# borc(X,Y) :- c(X,Y).
# nbc(X,Y) :- not bandc(X,Y).
# bandc(X,Y) :- b(X,Z), c(Z,Y).